from pydantic import BaseModel, ValidationError

class Book(BaseModel):
    id: int
    name: str 
    quantity: int = 0
    author: list[int] = []
    price: int = 0  
    description: str = ""
    rating_average: float = 0
    quantity_sold: int = 0
    review_count: int = 0
    image: list[str] = []  
    category: str = "Uncategorized" 


    
def create_book(data: dict)-> Book:
    # if "name" not in data or not data["name"]:
    #     return None
    # return Book(**data)
    try:
        if "name" not in data or not data["name"]:
            return None
        
        return Book(**data)
    except ValidationError as e:
        # print(f"Validation error: {e.json()}")
        return None