from sqlalchemy.orm import Session
from fastapi import HTTPException
from models import Item

NOT_FOUND = "Item not found"


def create_item(db: Session, item_create):
    """Create a new item in the database."""
    db_item = Item(name=item_create.name, price=item_create.price)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def get_items(db: Session):
    """Retrieve all items from the database."""
    return db.query(Item).all()


def get_item_by_id(db: Session, item_id: str):
    """Retrieve a specific item by its ID."""
    item = db.query(Item).filter(Item.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail=NOT_FOUND)
    return item


def update_item(db: Session, item_id: str, item_update):
    """Update an existing item in the database."""
    item = db.query(Item).filter(Item.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail=NOT_FOUND)
    item.name = item_update.name
    item.price = item_update.price
    db.commit()
    db.refresh(item)
    return item


def delete_item(db: Session, item_id: str):
    """Delete an item by its ID."""
    item = db.query(Item).filter(Item.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail=NOT_FOUND)
    db.delete(item)
    db.commit()
    return {"detail": "Item deleted"}
