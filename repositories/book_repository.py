from repositories.db_repository import FirebaseService
from models.book import Book, create_book
from collections import OrderedDict
from pydantic import ValidationError


class BookRepository:
    def __init__(self):
        self.collection_name = "books"

    def add_book(self, book_data: dict):
        # Tạo đối tượng book dựa trên role
        book = create_book(book_data)
        key = book.id
        FirebaseService.add_data(self.collection_name, key, book.dict())
        return {"message": "book created successfully."}


    def get_all_books(self):
        """
        Lấy tất cả sách từ Firebase và bỏ qua các sách thiếu name hoặc price.
        """
        # Lấy dữ liệu từ Firebase
        books_data = FirebaseService.get_data(self.collection_name)
        
        if isinstance(books_data, OrderedDict):
            # Duyệt qua từng sách, chỉ giữ sách hợp lệ
            valid_books = []
            for book_data in books_data.values():
                # Bỏ qua sách không có 'name' hoặc 'price'
                if not book_data.get('name') or not book_data.get('price'):
                    continue
                # Tạo đối tượng Book từ dữ liệu hợp lệ
                valid_books.append(create_book(book_data))
                # try:
                #     valid_books.append(create_book(book_data))
                # except ValidationError as e:
                #     print(f"Skipping invalid book data: {book_data}")
            
            return valid_books
        else:
            raise ValueError("Data from Firebase is not in expected format")

    def get_book_by_id(self, book_id: int):
        books_data = FirebaseService.get_data_by_key(self.collection_name, book_id)
        return create_book(books_data)

    def update_book_byID(self, book_id: int, book_data: dict):
        FirebaseService.update_data(self.collection_name, book_id, book_data)
        return {"message": "book updated successfully."}
    
    def update_book(self, book_data: dict):
        # Tạo đối tượng book và cập nhật dữ liệu
        book = create_book(book_data)
        key = book.id
        FirebaseService.update_data(self.collection_name, key, book.dict())
        return {"message": "book updated successfully."}

    def delete_book(self, book_id: int):
        FirebaseService.delete_data(self.collection_name, book_id)
        return {"message": "book deleted successfully."}


# Khởi tạo một instance cho repository
book_repository = BookRepository()
