from repositories.db_repository import FirebaseService

class OrderRepository:
    def __init__(self):
        self.collection_name = "orders"

    @staticmethod
    def create_order(self, order_data: dict):
        FirebaseService.add_data(self.collection_name, order_data)

    @staticmethod
    def get_all_orders(self):
        return FirebaseService.get_data(self.collection_name)

    @staticmethod
    def get_order_by_id(self, order_id: str):
        return FirebaseService.get_data_by_key(self.collection_name, order_id)

    @staticmethod
    def update_order(self, order_id: str, order_data: dict):
        FirebaseService.update_data(self.collection_name, order_id, order_data)

    @staticmethod
    def delete_order(self, order_id: str):
        FirebaseService.delete_data(self.collection_name, order_id)

