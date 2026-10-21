# Author: Chandler Harris
# Date: 10/18/2026
# File: routes.py
# Description:

from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from database import get_session
from .schemas import ProductRead
from .services import get_all_products, get_product_by_id

router = APIRouter(
    prefix="/products",
    tags=["Products"]
)


@router.get(
    "/",
    response_model=list[ProductRead],
    summary="Get all products"
)
def read_products(
    session: Session = Depends(get_session)
):
    return get_all_products(session)


@router.get(
    "/{product_id}",
    response_model=ProductRead,
    summary="Get a product by ID"
)
def read_product(
    product_id: int,
    session: Session = Depends(get_session)
):
    product = get_product_by_id(session, product_id)

    if product is None:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    return product
