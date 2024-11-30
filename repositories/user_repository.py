from repositories.db_repository import FirebaseService
from models.users import User  

class UserRepository:
    def __init__(self):
        self.collection_name = "user"

    def create_user(self, user_data: dict):
        # Xác thực dữ liệu đầu vào bằng class User
        user = User(**user_data)  # Tạo đối tượng User
        FirebaseService.add_data(self.collection_name, user.dict())  # Lưu vào Firebase

    def get_all_users(self):
        data = FirebaseService.get_data(self.collection_name)
        # Chuyển dữ liệu Firebase thành danh sách các đối tượng User
        return [User(**user) for user in data]

    def get_user_by_id(self, user_id: str):
        data = FirebaseService.get_data_by_key(self.collection_name, user_id)
        # Chuyển dữ liệu Firebase thành một đối tượng User
        return User(**data)

    def update_user(self, user_id: str, user_data: dict):
        user = User(**user_data)  # Xác thực và tạo đối tượng User
        FirebaseService.update_data(self.collection_name, user_id, user.dict())

    def delete_user(self, user_id: str):
        FirebaseService.delete_data(self.collection_name, user_id)
