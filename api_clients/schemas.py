from pydantic import BaseModel, ConfigDict, Field


class ProductResponse(BaseModel):
    model_config = ConfigDict(extra="ignore")
    id: int
    name: str
    category: str
    price: float
    stock: int


class UserResponse(BaseModel):
    model_config = ConfigDict(extra="ignore")
    id: int
    email: str


class LoginResponse(BaseModel):
    model_config = ConfigDict(extra="ignore")
    token: str = Field(min_length=1)
    user: UserResponse


class OrderResponse(BaseModel):
    model_config = ConfigDict(extra="ignore")
    id: int
    user_id: int
    status: str
    total: float
