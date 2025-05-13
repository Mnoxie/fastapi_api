from sqlalchemy import Column, Integer, String, Text, ForeignKey
from database import Base

class Product(Base):
    __tablename__ = "products_product"

    id = Column(Integer, primary_key=True, index=True)
    codigo = Column(String(255), unique=True, nullable=False)
    name = Column(String(255), nullable=False)
    description = Column(Text)
    price = Column(Integer)
    stock = Column(Integer)
    stock_min = Column(Integer)
    category_id = Column(Integer)
    image = Column(String(255), nullable=True)