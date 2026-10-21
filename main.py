from fastapi import FastAPI
from products.routes import router as product_router

app = FastAPI(
    title="Ulta Beauty Inventory and Order Management System",
    description=("RESTful API for managing customers, products, orders, inventory, and order items."),
    version="1.0.0"
)

app.include_router(product_router)



