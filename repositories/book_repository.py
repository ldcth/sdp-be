from repositories.db_repository import FirebaseService

class BookRepository:
    collection_name = "books"
    def __init__(self):
        self.collection_name = "books"

    @staticmethod
    def create_book(self, book_data: dict):
        FirebaseService.add_data(self.collection_name, book_data)

    @staticmethod
    def get_all_books(self):
        return FirebaseService.get_data(self.collection_name)

    @staticmethod
    def get_book_by_id(self, book_id: str):
        return FirebaseService.get_data_by_key(self.collection_name, book_id)

    @staticmethod
    def update_book(self, book_id: str, book_data: dict):
        FirebaseService.update_data(self.collection_name, book_id, book_data)

    @staticmethod
    def delete_book(self, book_id: str):
        FirebaseService.delete_data(self.collection_name, book_id)

# class BookRepository:
#     def __init__(self):
#         self.db = db.child("books")  # Sử dụng child() để truy cập collection

#     def get_all_books(self):
#         books = self.db.get()
#         return [book.val() for book in books.each()]

#     def get_book_by_id(self, book_id):
#         book = self.db.child(book_id).get()
#         return book.val() if book else None

#     def add_book(self, book_data):
#         self.db.child(book_data["id"]).set(book_data)
#         return book_data

#     def update_book(self, book_id, book_data):
#         self.db.child(book_id).update(book_data)
#         return book_data

#     def delete_book(self, book_id):
#         self.db.child(book_id).remove()

