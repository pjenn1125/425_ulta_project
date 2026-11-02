# Author: Chandler Harris
# Date: 10/18/2026
# File: services.py
# Description: Contains the functions used to retrieve product records from the database.

from sqlmodel import Session, select

from .models import Product


def get_all_products(session: Session):
    statement = select(Product)
    products = session.exec(statement).all()
    return products


def get_product_by_id(session: Session, product_id: int):
    product = session.get(Product, product_id)
    return product


def get_paginated_products(
    session: Session,
    offset: int,
    limit: int,
    sort: list[str],
):
    sort_fields = {
        "product_id": Product.product_id,
        "product_name": Product.product_name,
        "brand": Product.brand,
        "price": Product.price,
        "category": Product.category,
    }
    statement = select(Product)

    for sort_option in sort:
        descending = sort_option.startswith("-")
        field_name = sort_option[1:] if descending else sort_option
        field = sort_fields.get(field_name)
        if field is None:
            raise ValueError(f"Unsupported sort field: {field_name}")
        statement = statement.order_by(
            field.desc() if descending else field.asc()
        )

    return session.exec(statement.offset(offset).limit(limit)).all()


def search_products(session: Session, query: str):
    search_term = f"%{query.strip()}%"
    statement = select(Product).where(
        Product.product_name.ilike(search_term)
        | Product.brand.ilike(search_term)
        | Product.category.ilike(search_term)
    )
    return session.exec(statement).all()
