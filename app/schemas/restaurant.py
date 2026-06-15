from pydantic import BaseModel

class RestaurantBase(BaseModel):
    name: str
    description: str
    image: str = "default.jpg"

class Restaurant(RestaurantBase):
    id: int

    class Config:
        from_attributes = True