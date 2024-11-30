from repositories.db_repository import FirebaseService
from models.order import order, create_order
from collections import OrderedDict
from pydantic import ValidationError


class OrderRepository:
    def __init__(self):
        self.collection_name = "orders"

    def add_order(self, order_data: dict):
        order = create_order(order_data)
        key = order.id
        FirebaseService.add_data(self.collection_name, key, order.dict())
        return {"message": "order created successfully."}


    def get_all_orders(self):
        # Lấy dữ liệu từ Firebase
        orders_data = FirebaseService.get_data(self.collection_name)
        
        if isinstance(orders_data, OrderedDict):
            # Duyệt qua từng sách, chỉ giữ sách hợp lệ
            valid_orders = []
            for order_data in orders_data.values():
                # Bỏ qua sách không có 'name' hoặc 'price'
                if not order_data.get('name') or not order_data.get('price'):
                    continue
                # Tạo đối tượng order từ dữ liệu hợp lệ
                valid_orders.append(create_order(order_data))
            
            return valid_orders
        else:
            raise ValueError("Data from Firebase is not in expected format")

    def get_order_by_id(self, order_id: int):
        orders_data = FirebaseService.get_data_by_key(self.collection_name, order_id)
        return create_order(orders_data)

    def update_order_byID(self, order_id: int, order_data: dict):
        FirebaseService.update_data(self.collection_name, order_id, order_data)
        return {"message": "order updated successfully."}
    
    def update_order(self, order_data: dict):
        # Tạo đối tượng order và cập nhật dữ liệu
        order = create_order(order_data)
        key = order.id
        FirebaseService.update_data(self.collection_name, key, order.dict())
        return {"message": "order updated successfully."}

    def delete_order(self, order_id: int):
        FirebaseService.delete_data(self.collection_name, order_id)
        return {"message": "order deleted successfully."}


# Khởi tạo một instance cho repository
order_repository = OrderRepository()
