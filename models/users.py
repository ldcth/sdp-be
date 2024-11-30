from pydantic import BaseModel, Field, field_validator
from typing import List, Optional, Type

# Lớp cha chung User
class User(BaseModel):
    id: str
    name: str
    username: str
    password: str
    date: str
    gender: bool
    info: str
    phone: str
    role: str
    
    @field_validator("phone")
    def validate_phone(cls, value):
        if not value.isdigit() or len(value) < 10:
            raise ValueError("Phone number must contain at least 10 digits and be numeric.")
        return value

    @field_validator("date")
    def validate_date(cls, value):
        # Optional: Kiểm tra định dạng ngày (yyyy-mm-dd) bằng regex hoặc parser
        return value

# Lớp con Admin
class Admin(User):
    permissions: List[str]  # Danh sách quyền của Admin
    managed_users: Optional[List[str]] = []  # Danh sách ID người dùng mà Admin quản lý


# Lớp con RegularUser
class RegularUser(User):
    # subscription_type: Optional[str] = None  # Loại gói đăng ký (nếu có)
    # wishlist: List[str]  # Danh sách sách mong muốn
    cart: List[str]
    history: List[str]


# Lớp con DeliveryMan
class DeliveryMan(User):
    # vehicle: str  # Loại phương tiện giao hàng
    history: List[str]
    region: str
    # rating: List[int]


# Factory function để tạo đối tượng User dựa trên role
def create_user(user_data: dict) -> User:
    role_to_class: dict[str, Type[User]] = {
        "Admin": Admin,
        "User": RegularUser,
        "DeliveryMan": DeliveryMan,
    }

    role = user_data.get('role')
    if role not in role_to_class:
        raise ValueError(f"Unknown role: {role}")

    # Lấy class tương ứng với role và khởi tạo đối tượng
    user_class = role_to_class[role]
    return user_class(**user_data)

