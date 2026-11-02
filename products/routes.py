# Author: Chandler Harris
# Date: 10/18/2026
# File: routes.py
# Description: Defines the product API endpoints for retrieving all products and a specific product.

from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from database import get_session
from .schemas import ProductRead, ProductCreate, ProductUpdate
from .services import (get_all_products,
                       get_product_by_id,
                       create_product,
                       update_product,
                       delete_product)

router = APIRouter(
    prefix="/products",
    tags=["Products"]
)


@router.get(
    "/",
    response_model=list[ProductRead],
    summary="Get all products")

def read_products(
    session: Session = Depends(get_session)):
    return get_all_products(session)


@router.get(
    "/{product_id}",
    response_model=ProductRead,
    summary="Get a product by ID")

def read_product(
    product_id: int,
    session: Session = Depends(get_session)):

    product = get_product_by_id(session, product_id)

    #check if the product exists
    if product is None:
        raise HTTPException(
            status_code=404,
            detail="Product not found")

    return product

#create products
@router.post(
    "/",
    response_model=ProductRead,
    status_code=201,
    summary="Create a new product")

def create_product_route(
        product_data: ProductCreate,
        session: Session = Depends(get_session)):

        return create_product(session, product_data)

#update products
@router.put(
    "/{product_id}",
    response_model=ProductRead,
    summary="Update a product")

def update_product_route(
        product_id: int,
        product_data: ProductUpdate,
        session: Session = Depends(get_session)):

        updated_product= update_product(session, product_id, product_data)

        if updated_product is None:
            raise HTTPException(
                status_code=404,
                detail="Product not found")
        return updated_product

#delete product
@router.delete(
    "/{product_id}",
    status_code=200,
    summary="Delete a product")

def delete_product_route(
        product_id: int,
        session: Session = Depends(get_session)):

        deleted_product= delete_product(session, product_id)

        # checks if the product exists
        if deleted_product is None:
            raise HTTPException(
                status_code=404,
                detail="Product not found")
        return {'message': 'Product deleted'}
