from pathlib import Path
from fastapi import Depends, FastAPI, HTTPException, Query
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session
from .db import Base, engine, get_db
from .models import Order, OrderItem, Product, User
from .schemas import LoginRequest, OrderCreate, OrderOut, ProductOut
from .seed import seed

app = FastAPI(title="E-Commerce SDET Demo API", version="1.0.0")
app.mount("/static", StaticFiles(directory=Path(__file__).parent / "static"), name="static")

@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)
    seed()

@app.get("/", include_in_schema=False)
def home():
    return FileResponse(Path(__file__).parent / "static" / "index.html")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/api/auth/login")
def login(payload: LoginRequest, db: Session = Depends(get_db)):
    user = db.query(User).filter_by(email=payload.email, password=payload.password).first()
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {"token": f"test-token-{user.id}", "user": {"id": user.id, "email": user.email}}

@app.get("/api/products", response_model=list[ProductOut])
def products(category: str | None = Query(default=None), q: str | None = Query(default=None), db: Session = Depends(get_db)):
    query = db.query(Product)
    if category:
        query = query.filter(Product.category == category)
    if q:
        query = query.filter(Product.name.ilike(f"%{q}%"))
    return query.order_by(Product.id).all()

@app.get("/api/products/{product_id}", response_model=ProductOut)
def product(product_id: int, db: Session = Depends(get_db)):
    item = db.get(Product, product_id)
    if not item:
        raise HTTPException(status_code=404, detail="Product not found")
    return item

@app.post("/api/orders", response_model=OrderOut, status_code=201)
def create_order(payload: OrderCreate, db: Session = Depends(get_db)):
    user = db.get(User, payload.user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    total = 0.0
    items = []
    for request_item in payload.items:
        product = db.get(Product, request_item.product_id)
        if not product:
            raise HTTPException(status_code=404, detail=f"Product {request_item.product_id} not found")
        if product.stock < request_item.quantity:
            raise HTTPException(status_code=409, detail=f"Insufficient stock for {product.name}")
        total += float(product.price) * request_item.quantity
        product.stock -= request_item.quantity
        items.append(OrderItem(product_id=product.id, quantity=request_item.quantity, unit_price=product.price))
    order = Order(user_id=user.id, status="PLACED", total=round(total, 2), items=items)
    db.add(order)
    db.commit()
    db.refresh(order)
    return order

@app.get("/api/orders/{order_id}", response_model=OrderOut)
def get_order(order_id: int, db: Session = Depends(get_db)):
    order = db.get(Order, order_id)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order
