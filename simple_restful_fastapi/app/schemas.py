# Pydantic schemas for request and response validation
from pydantic import BaseModel


class ItemCreate(BaseModel):
    name: str
    price: float


class ItemResponse(BaseModel):
    id: str
    name: str
    price: float
