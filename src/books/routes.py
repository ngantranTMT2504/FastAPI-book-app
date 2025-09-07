from fastapi import APIRouter, status, HTTPException
from typing import List
from src.books.book_data import books
from src.books.schemas import Book, BookUpdateModel

book_router = APIRouter()

@book_router.get("", response_model = List[Book])
async def get_all():
    return books

@book_router.post("" , status_code = status.HTTP_201_CREATED)
async def create_book(book : Book):
    new_book = book.model_dump()
    books.append(new_book)
    return new_book