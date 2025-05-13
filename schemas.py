from pydantic import BaseModel
from typing import Optional

class ProductSchema(BaseModel):
    id: int
    codigo: str
    name: str
    description: str
    price: int
    stock: int
    stock_min: Optional[int]
    category_id: int
    image: Optional[str]

    class Config:
        orm_mode = True
