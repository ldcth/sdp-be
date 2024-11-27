from fastapi import APIRouter, HTTPException
from models.book import Book
from repositories.book_repository import book_repository

router = APIRouter()

@router.get("/books")
def get_books():
    books = book_repository.get_all_books()
    return books

@router.get("/books/{book_id}")
def get_book(book_id: str):
    book = book_repository.get_book_by_id(book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@router.post("/books")
def create_book(book: Book):
    return book_repository.add_book(book.dict())

@router.put("/books/{book_id}")
def update_book(book_id: str, book: Book):
    return book_repository.update_book(book_id, book.dict())

@router.delete("/books/{book_id}")
def delete_book(book_id: str):
    book_repository.delete_book(book_id)
    return {"message": "Book deleted successfully"}