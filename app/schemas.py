from pydantic import BaseModel, EmailStr, Field

class LoginRequest(BaseModel):
    email: EmailStr
    password: str = Field(min_length=1)

class ProductOut(BaseModel):
    id: int
    name: str
    category: str
    price: float
    stock: int
    model_config = {"from_attributes": True}

class OrderItemIn(BaseModel):
    product_id: int
    quantity: int = Field(gt=0, le=20)

class OrderCreate(BaseModel):
    user_id: int
    items: list[OrderItemIn] = Field(min_length=1)

class OrderOut(BaseModel):
    id: int
    user_id: int
    status: str
    total: float
    model_config = {"from_attributes": True}
