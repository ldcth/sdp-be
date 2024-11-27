from fastapi import APIRouter, HTTPException
from strategies.role_strategy import AdminStrategy, UserStrategy, UserRole

router = APIRouter()

@router.get("/user-action/{role}")
def perform_role_action(role: str):
    if role == "admin":
        strategy = AdminStrategy()
    elif role == "user":
        strategy = UserStrategy()
    else:
        raise HTTPException(status_code=400, detail="Invalid role")

    user_role = UserRole(strategy)
    return {"action": user_role.execute_action()}