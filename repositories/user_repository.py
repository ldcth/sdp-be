from db_repository import FirebaseService

class UserRepository:
    def __init__(self):
        self.collection_name = "users"

    @staticmethod
    def create_user(self, user_data: dict):
        FirebaseService.add_data(self.collection_name, user_data)

    @staticmethod
    def get_all_users(self):
        return FirebaseService.get_data(self.collection_name)

    @staticmethod
    def get_user_by_id(self, user_id: str):
        return FirebaseService.get_data_by_key(self.collection_name, user_id)

    @staticmethod
    def update_user(self, user_id: str, user_data: dict):
        FirebaseService.update_data(self.collection_name, user_id, user_data)

    @staticmethod
    def delete_user(self, user_id: str):
        FirebaseService.delete_data(self.collection_name, user_id)