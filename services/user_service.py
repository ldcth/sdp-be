from core.config import auth
from services.firebase_service import FirebaseService

class UserService:
    collection_name = "users"

    @staticmethod
    def create_user(email: str, password: str, user_data: dict):
        # Tạo tài khoản người dùng trên Firebase Auth
        user = auth.create_user_with_email_and_password(email, password)
        user_data["uid"] = user["localId"]
        FirebaseService.add_data(UserService.collection_name, user_data)

    @staticmethod
    def login(email: str, password: str):
        return auth.sign_in_with_email_and_password(email, password)
