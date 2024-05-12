from sqlalchemy import Column, Float, String
from database import Base


class Item(Base):
    __tablename__ = "items"
    id = Column(String, primary_key=True, index=True)
    name = Column(String, index=True)
    price = Column(Float)
