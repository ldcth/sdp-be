from repositories.db_repository import FirebaseService
from models.users import User, create_user
from collections import OrderedDict


class UserRepository:
    def __init__(self):
        self.collection_name = "user"

    def add_user(self, user_data: dict):
        # Tạo đối tượng User dựa trên role
        user = create_user(user_data)
        key = user.id
        FirebaseService.add_data(self.collection_name, key, user.dict())
        return {"message": "User created successfully."}

    def get_all_users(self):
        # Lấy tất cả người dùng từ Firebase
        users_data = FirebaseService.get_data(self.collection_name)
        # return [create_user(user) for user in users_data]
        if isinstance(users_data, OrderedDict):
        # Duyệt qua các giá trị trong OrderedDict và tạo đối tượng User
            return [create_user(user_data) for user_data in users_data.values()]
        else:
            raise ValueError("Data from Firebase is not in expected format")


    def get_user_by_id(self, user_id: int):
        users_data = FirebaseService.get_data_by_key(self.collection_name, user_id)
        # user_get = db.child(self.collection_name).order_by_child("id").equal_to(user_id).get()
        # # print(user_get)
        # for user in user_get.each():
        #     # print(user.key())  # In khóa của mỗi bản ghi
        #     # print(user.val()) 
        #     return create_user(user.val())
        return create_user(users_data.val())

    def update_user(self, user_id: int, user_data: dict):
        # Tạo đối tượng User và cập nhật dữ liệu
        usernew = create_user(user_data)
        # user_get = db.child(self.collection_name).order_by_child("id").equal_to(user_id).get()
        # # print(user_get)
        # for user in user_get.each():
        #     tmp_key = user.key()
        #     db.child("user").child(tmp_key).update(usernew.dict())
        FirebaseService.update_data(self.collection_name, user_id, usernew.dict())
        return {"message": "User updated successfully."}
    
    def update_user_byID(self, user_id: int, user_data: dict):
        FirebaseService.update_data(self.collection_name, user_id, user_data)
        return {"message": "User updated successfully."}

    def delete_user(self, user_id: int):
        FirebaseService.delete_data(self.collection_name, user_id)
        return {"message": "User deleted successfully."}


# Khởi tạo một instance cho repository
user_repository = UserRepository()
