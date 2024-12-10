from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
import schemas, crud

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/carts/", response_model=schemas.CartResponse)
def add_to_cart(cart: schemas.CartCreate, db: Session = Depends(get_db)):
    return crud.add_to_cart(db, cart)

@router.get("/carts/{user_id}", response_model=list[schemas.CartResponse])
def read_cart(user_id: int, db: Session = Depends(get_db)):
    return crud.get_cart_by_user(db, user_id)

@router.delete("/carts/{cart_id}")
def delete_cart_item(cart_id: int, db: Session = Depends(get_db)):
    db_cart = crud.delete_cart_item(db, cart_id)
    if db_cart is None:
        raise HTTPException(status_code=404, detail="Cart item not found")
    return {"detail": "Cart item deleted successfully"}
