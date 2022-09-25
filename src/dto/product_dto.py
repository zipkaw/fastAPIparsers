from pydantic import BaseModel


class ProductDto(BaseModel):
    brand: str
    description: str
    price: str
    sex: str
    type: str


class ProductDbDto(ProductDto):
    _id: str
