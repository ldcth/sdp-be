from services.firebase_service import FirebaseService

class BookService:
    collection_name = "books"

    @staticmethod
    def create_book(book_data: dict):
        FirebaseService.add_data(BookService.collection_name, book_data)

    @staticmethod
    def get_all_books():
        return FirebaseService.get_data(BookService.collection_name)

    @staticmethod
    def get_book_by_id(book_id: str):
        return FirebaseService.get_data_by_key(BookService.collection_name, book_id)

    @staticmethod
    def update_book(book_id: str, book_data: dict):
        FirebaseService.update_data(BookService.collection_name, book_id, book_data)

    @staticmethod
    def delete_book(book_id: str):
        FirebaseService.delete_data(BookService.collection_name, book_id)
