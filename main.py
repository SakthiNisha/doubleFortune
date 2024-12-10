from fastapi import FastAPI
from routers import users, products, carts, orders

app = FastAPI()

# Include routers
app.include_router(users.router, prefix="/api", tags=["users"])
app.include_router(products.router, prefix="/api", tags=["products"])
app.include_router(carts.router, prefix="/api", tags=["carts"])
app.include_router(orders.router, prefix="/api", tags=["orders"])

@app.get("/")
def read_root():
    return {"message": "Welcome to Double Fortune eCommerce API"}
