
from fastapi import FastAPI
from database import create_db_and_tables

from products.routes import router as product_router
from customers.routes import router as customer_router
from orders.routes import router as order_router
from inventory.routes import router as inventory_router
from order_items.routes import router as order_item_router


app = FastAPI(
    title="Ulta Beauty Inventory and Order Management System",
    description="RESTful API for managing customers, products, orders, inventory, and order items.",
    version="1.0.0"
)

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

app.include_router(product_router)
app.include_router(customer_router)
app.include_router(order_router)
app.include_router(inventory_router)
app.include_router(order_item_router)



