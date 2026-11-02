# Author: Chandler Harris
# Date: 10/18/2026
# File: services.py
# Description: Contains the functions used to retrieve product records from the database.

from sqlmodel import Session, select
from .models import Product
from .schemas import ProductUpdate, ProductCreate

#retrieve all product records from the database
def get_all_products(session: Session):
    statement = select(Product)
    products = session.exec(statement).all()
    return products

#get product by id
def get_product_by_id(session: Session, product_id: int):
    product = session.get(Product, product_id)
    return product

#create the products
def create_product(session: Session, product_data: ProductCreate):
    product = Product(**product_data.model_dump())
    session.add(product)
    session.commit()
    session.refresh(product)
    return product

#updates an existing product using its product id
def update_product(session: Session, product_id: int, product_data: ProductUpdate):
    product = session.get(Product, product_id)

    #checks if the product exists
    if product is None:
        return None

    product_data_dict = product_data.model_dump(exclude_unset=True)

    for key, value in product_data_dict.items():
        setattr(product, key, value)

    session.add(product)
    session.commit()
    session.refresh(product)
    return product

#removes an existing product from the database
def delete_product(session: Session, product_id: int):
    product = session.get(Product, product_id)

    if product is None:
        return None

    #delete the product from the database session
    session.delete(product)

    #save the deletion to the database
    session.commit()
    return product
