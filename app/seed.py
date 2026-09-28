from .db import Base, SessionLocal, engine
from .models import Product, User

def seed():
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    try:
        if not db.query(User).filter_by(email="qa@example.com").first():
            db.add(User(email="qa@example.com", password="Password123"))
        if db.query(Product).count() == 0:
            db.add_all([
                Product(name="Laptop Pro", category="Electronics", price=899.99, stock=15),
                Product(name="Wireless Mouse", category="Accessories", price=29.99, stock=50),
                Product(name="Mechanical Keyboard", category="Accessories", price=79.99, stock=25),
                Product(name="USB-C Hub", category="Accessories", price=39.99, stock=40),
            ])
        db.commit()
    finally:
        db.close()
