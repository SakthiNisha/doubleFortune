from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class UserCreate(BaseModel):
    name: str
    email: str
    password: str

class UserResponse(BaseModel):
    id: int
    name: str
    email: str

    class Config:
        orm_mode = True

# Product Schema for creation
class ProductCreate(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    stock: int

# Product Schema for response
class ProductResponse(BaseModel):
    id: int
    name: str
    description: Optional[str]
    price: float
    stock: int

    class Config:
        orm_mode = True

# Cart Schema for creation
class CartCreate(BaseModel):
    user_id: int
    product_id: int
    quantity: int

# Cart Schema for response
class CartResponse(BaseModel):
    id: int
    user_id: int
    product_id: int
    quantity: int

    class Config:
        orm_mode = True

# Order Schema for creation
class OrderCreate(BaseModel):
    user_id: int
    total_amount: float

# Order Schema for response
class OrderResponse(BaseModel):
    id: int
    user_id: int
    total_amount: float
    created_at: datetime

    class Config:
        orm_mode = True

