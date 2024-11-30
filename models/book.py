from pydantic import BaseModel

class Book(BaseModel):
    id: str
    name: str
    quantity: int
    author: list[str]  # List of author IDs
    price: float
    description: str
    rating: float
    quantity_sold: int
    review_count: int
    image: list[str]  # List of image URLs
    category: str
    
