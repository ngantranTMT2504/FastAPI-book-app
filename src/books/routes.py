from fastapi import APIRouter, status, HTTPException
from typing import List
from fastapi.params import Depends
from sqlmodel.ext.asyncio.session import AsyncSession
from src.books.schemas import Book, BookUpdateModel
from src.books.service import BookService
from src.db.main import get_session

book_router = APIRouter()
book_service = BookService()

@book_router.get("/", response_model = List[Book])
async def get_all(session: AsyncSession = Depends(get_session)):
    books = await book_service.get_all_books(session)
    return books

@book_router.post("/" , status_code = status.HTTP_201_CREATED)
async def create_book(book : Book, session: AsyncSession = Depends(get_session)) -> dict:
    new_book = await book_service.create_book(book, session)
    return new_book

@book_router.get("/{book_uid}")
async def get_book(book_uid: str, session: AsyncSession = Depends(get_session)) -> dict:
    book = await book_service.get_book_by_id(book_uid, session)
    if book:
        return book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")

@book_router.put("/{book_uid}")
async def update_book(book_uid: str, book: BookUpdateModel, session: AsyncSession = Depends(get_session)):
    book_updated = await book_service.update_book(book_uid, book, session)
    if book_updated:
        return book_updated
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")

@book_router.delete("/{book_uid}")
async def delete_book(book_uid: str, session: AsyncSession = Depends(get_session)):
    book_deleted = await book_service.delete_book(book_uid, session)
    if book_deleted:
        return book_deleted
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")