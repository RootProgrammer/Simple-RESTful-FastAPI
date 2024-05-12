from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from database import SessionLocal
from schemas import ItemCreate, ItemResponse
from operations.item_operations import (
    create_item,
    get_items,
    get_item_by_id,
    update_item,
    delete_item,
)

router = APIRouter()


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@router.post("/items/", response_model=ItemResponse, status_code=201)
async def create_item_route(item: ItemCreate, db: Session = Depends(get_db)):
    return create_item(db, item)


@router.get("/items/", response_model=List[ItemResponse])
async def read_items_route(db: Session = Depends(get_db)):
    return get_items(db)


@router.get("/items/{item_id}", response_model=ItemResponse)
async def read_item_route(item_id: str, db: Session = Depends(get_db)):
    item = get_item_by_id(db, item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@router.put("/items/{item_id}", response_model=ItemResponse)
async def update_item_route(
    item_id: str, item: ItemCreate, db: Session = Depends(get_db)
):
    return update_item(db, item_id, item)


@router.delete("/items/{item_id}", status_code=204)
async def delete_item_route(item_id: str, db: Session = Depends(get_db)):
    return delete_item(db, item_id)
