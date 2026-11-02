# Author: Chandler Harris, Jennifer P.
# Date: 10/18/2026
# File: routes.py
# Description: Defines the product API endpoints for retrieving all products,
# pagination, sorting, and search functionality.

from typing import List, Optional
from fastapi import APIRouter, Depends, Query
from sqlmodel import Session, select, or_
from database import get_session
from .models import Product
from .schemas import ProductRead

router = APIRouter(
    prefix="/products",
    tags=["Products"]
)

# Get all products (Lab 2)
@router.get(
    "/",
    response_model=List[ProductRead],
    summary="Get all products"
)
def read_products(session: Session = Depends(get_session)):
    return session.exec(select(Product)).all()

# Pagination and sorting (Lab 3 - Resource A)
@router.get(
    "/paginate",
    response_model=List[ProductRead],
    summary="Paginated and sorted products"
)
def paginate_products(
    session: Session = Depends(get_session),
    offset: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=100),
    sort: Optional[str] = Query(
        None,
        description="Comma-separated fields. Use '-' prefix for descending. Example: 'price,-brand'"
    )
):
    query = select(Product)

    # Sorting logic
    if sort:
        sort_fields = sort.split(",")
        for field in sort_fields:
            desc = field.startswith("-")
            field_name = field[1:] if desc else field

            if hasattr(Product, field_name):
                column = getattr(Product, field_name)
                query = query.order_by(column.desc() if desc else column)

    # Pagination logic
    query = query.offset(offset).limit(limit)

    return session.exec(query).all()


# Search products (Lab 3 - Resource B)
@router.get(
    "/search",
    response_model=List[ProductRead],
    summary="Search products by name, brand, or category"
)
def search_products_route(
    session: Session = Depends(get_session),
    q: str = Query(..., min_length=1)
):
    pattern = f"%{q}%"

    query = select(Product).where(
        or_(
            Product.product_name.ilike(pattern),
            Product.brand.ilike(pattern),
            Product.category.ilike(pattern)
        )
    )

    return session.exec(query).all()