from sqlalchemy.orm import Session
from models import User
from schemas import UserCreate
from models import Product
from schemas import ProductCreate
from models import Cart
from schemas import CartCreate
from models import Order
from schemas import OrderCreate
from datetime import datetime

def create_user(db: Session, user: UserCreate):
    db_user = User(name=user.name, email=user.email, password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

# Create a product
def create_product(db: Session, product: ProductCreate):
    db_product = Product(
        name=product.name,
        description=product.description,
        price=product.price,
        stock=product.stock
    )
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

# Get a product by ID
def get_product(db: Session, product_id: int):
    return db.query(Product).filter(Product.id == product_id).first()

# Get all products
def get_products(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Product).offset(skip).limit(limit).all()

# Update a product
def update_product(db: Session, product_id: int, product: ProductCreate):
    db_product = db.query(Product).filter(Product.id == product_id).first()
    if db_product:
        db_product.name = product.name
        db_product.description = product.description
        db_product.price = product.price
        db_product.stock = product.stock
        db.commit()
        db.refresh(db_product)
    return db_product

# Delete a product
def delete_product(db: Session, product_id: int):
    db_product = db.query(Product).filter(Product.id == product_id).first()
    if db_product:
        db.delete(db_product)
        db.commit()
    return db_product   

# Add item to cart
def add_to_cart(db: Session, cart: CartCreate):
    db_cart = Cart(user_id=cart.user_id, product_id=cart.product_id, quantity=cart.quantity)
    db.add(db_cart)
    db.commit()
    db.refresh(db_cart)
    return db_cart

# Get cart by user ID
def get_cart_by_user(db: Session, user_id: int):
    return db.query(Cart).filter(Cart.user_id == user_id).all()

# Delete cart item
def delete_cart_item(db: Session, cart_id: int):
    db_cart = db.query(Cart).filter(Cart.id == cart_id).first()
    if db_cart:
        db.delete(db_cart)
        db.commit()
    return db_cart     

# Create an order
def create_order(db: Session, order: OrderCreate):
    db_order = Order(
        user_id=order.user_id,
        total_amount=order.total_amount,
        created_at=datetime.utcnow()
    )
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order

# Get an order by ID
def get_order(db: Session, order_id: int):
    return db.query(Order).filter(Order.id == order_id).first()

# Get all orders by user ID
def get_orders_by_user(db: Session, user_id: int):
    return db.query(Order).filter(Order.user_id == user_id).all()

# Delete an order
def delete_order(db: Session, order_id: int):
    db_order = db.query(Order).filter(Order.id == order_id).first()
    if db_order:
        db.delete(db_order)
        db.commit()
    return db_order