from fastapi import APIRouter, HTTPException
from models.users import User
from repositories.user_repository import user_repository

router = APIRouter()

@router.get("/users", response_model=list[User])
def get_users():
    users = user_repository.get_all_users()
    return users

@router.get("/users/{user_id}", response_model=User)
def get_user(user_id: str):
    user = user_repository.get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found.")
    return user

@router.post("/users", response_model=dict)
def create_user(user: User):
    return user_repository.add_user(user.dict())

@router.put("/users/{user_id}", response_model=dict)
def update_user(user_id: str, user: User):
    return user_repository.update_user(user_id, user.dict())

@router.delete("/users/{user_id}", response_model=dict)
def delete_user(user_id: str):
    return user_repository.delete_user(user_id)
