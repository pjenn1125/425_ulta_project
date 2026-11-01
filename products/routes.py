# Author: Chandler Harris, Jennifer P.
# Date: 10/18/2026
# File: routes.py
# Description: Defines the product API endpoints for retrieving all products,
# pagination, sorting, and search functionality.

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import Session
from database import get_session
from .schemas import ProductRead
from .services import (
    get_all_products,
    get_product_by_id,
    get_paginated_products,
    search_products
)

router = APIRouter(
    prefix="/products",
    tags=["Products"]
)

# ---------------------------------------------------------
# GET ALL PRODUCTS (Lab 2)
# ---------------------------------------------------------
@router.get(
    "/",
    response_model=list[ProductRead],
    summary="Get all products"
)
def read_products(session: Session = Depends(get_session)):
    return get_all_products(session)


# PAGINATION + SORTING (Lab 3 - Added by Jennifer P.)
@router.get(
    "/paginate",
    response_model=list[ProductRead],
    summary="Paginated and sorted products"
)
def paginate_products(
    session: Session = Depends(get_session),
    offset: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=100),
    sort: list[str] = Query(["price"])  # Example: ?sort=price&sort=-brand
):
    return get_paginated_products(session, offset, limit, sort)


# SEARCH PRODUCTS (Lab 3 - Added by Jennifer P.
@router.get(
    "/search",
    response_model=list[ProductRead],
    summary="Search products by name, brand, or category"
)
def search_products_route(
    q: str = Query(..., min_length=1),
    session: Session = Depends(get_session)
):
    return search_products(session, q)
