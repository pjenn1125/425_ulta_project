# Author: Chandler Harris
# Date: 10/18/2026
# File: services.py
# Description:

from sqlmodel import Session, select
from .models import Product


def get_all_products(session: Session):
    statement = select(Product)
    products = session.exec(statement).all()
    return products


def get_product_by_id(session: Session, product_id: int):
    product = session.get(Product, product_id)
    return product
