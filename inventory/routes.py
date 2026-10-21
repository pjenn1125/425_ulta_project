# Author: Chandler Harris
# Date: 10/20/2026
# File: routes.py
# Description: Defines the inventory API endpoints for retrieving inventory records and product inventory.

from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select

from database import get_session
from .schemas import InventoryRead
from .services import get_all_inventory, get_inventory_by_id

router = APIRouter(
    prefix="/inventory",
    tags=["Inventory"]
)


@router.get(
    "/",
    response_model=List[InventoryRead],
    summary="Get all inventory records"
)
def read_inventory(
    session: Session = Depends(get_session)
):
    return get_all_inventory(session)


@router.get(
    "/{inventory_id}",
    response_model=InventoryRead,
    summary="Get an inventory record by ID"
)
def read_inventory_record(
    inventory_id: int,
    session: Session = Depends(get_session)
):
    inventory = get_inventory_by_id(session, inventory_id)

    if inventory is None:
        raise HTTPException(
            status_code=404,
            detail="Inventory record not found"
        )

    return inventory

#end points

from inventory.models import Inventory
from inventory.schemas import InventoryRead


@router.get("/{product_id}/inventory", response_model=InventoryRead, summary="Get inventory for a product")
def get_product_inventory(
    product_id: int,
    session: Session = Depends(get_session)
):
    inventory = session.exec(
        select(Inventory).where(Inventory.product_id == product_id)
    ).first()

    if inventory is None:
        raise HTTPException(
            status_code=404,
            detail="Inventory not found for this product"
        )

    return inventory
