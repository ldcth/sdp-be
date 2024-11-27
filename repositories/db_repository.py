from core.config import db

#crud
class FirebaseService:
    @staticmethod
    def add_data(collection: str, data: dict):
        """
        Thêm dữ liệu vào collection trong Firebase.
        """
        db.child(collection).push(data)

    @staticmethod
    def get_data(collection: str):
        """
        Lấy tất cả dữ liệu từ collection.
        """
        return db.child(collection).get().val()

    @staticmethod
    def get_data_by_key(collection: str, key: str):
        """
        Lấy dữ liệu theo key từ collection.
        """
        return db.child(collection).child(key).get().val()

    @staticmethod
    def update_data(collection: str, key: str, data: dict):
        """
        Cập nhật dữ liệu trong collection.
        """
        db.child(collection).child(key).update(data)

    @staticmethod
    def delete_data(collection: str, key: str):
        """
        Xóa dữ liệu theo key trong collection.
        """
        db.child(collection).child(key).remove()
