from sqlalchemy import Column, Integer, String, Text, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Product(Base):
    __tablename__ = 'products_product'

    id = Column(Integer, primary_key=True)
    name = Column(String(200), nullable=True)
    price = Column(Integer, nullable=True)
    description = Column(Text, nullable=True)
    image_url = Column(String, nullable=True)
    discount = Column(String(200), nullable=True)
    url = Column(String, nullable=True)
    date = Column(Date, nullable=True)
