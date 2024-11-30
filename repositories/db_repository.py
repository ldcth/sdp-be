from core.config import db

#crud
class FirebaseService:
    @staticmethod
    def add_data(collection: str, key: int, data: dict):
        """
        Thêm dữ liệu vào collection trong Firebase.
        """
        # db.child(collection).push(data)
        db.child(collection).child(key).set(data)

    @staticmethod
    def get_data(collection: str):
        """
        Lấy tất cả dữ liệu từ collection.
        """
        return db.child(collection).get().val()

    @staticmethod
    def get_data_by_key(collection: str, key: int):
        """
        Lấy dữ liệu theo key từ collection.
        """
        # temp = db.child(collection).order_by_child("id").equal_to(key).get()
        # for tmp in temp.each():
        #     data = tmp.val()

        data_get = db.child(collection).order_by_child("id").equal_to(key).get()
        for temp in data_get.each():
            tmp = temp.val() 
            # print(tmp)
            return tmp

    @staticmethod
    def update_data(collection: str, key: int, data: dict):
        """
        Cập nhật dữ liệu trong collection.
        """
        data_get = db.child(collection).order_by_child("id").equal_to(key).get()
        for temp in data_get.each():
            tmp_key = temp.key()
            db.child(collection).child(tmp_key).update(data)

    @staticmethod
    def delete_data(collection: str, key: int):
        """
        Xóa dữ liệu theo key trong collection.
        """
        data_get = db.child(collection).order_by_child("id").equal_to(key).get()
        for temp in data_get.each():
            tmp_key = temp.key()
            db.child(collection).child(tmp_key).remove()
