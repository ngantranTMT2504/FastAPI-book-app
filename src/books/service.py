from sqlmodel.ext.asyncio.session import AsyncSession
from .schemas import BookCreateModel, BookUpdateModel
from sqlmodel import select
from .models import Book
from datetime import datetime

class BookService:
    async def get_all_books(self, session: AsyncSession):
        statement = select(Book).order_by(Book.create_at)
        result = await session.exec(statement)
        return result.all()

    async def get_book_by_id(self, book_uid: str, session: AsyncSession):
        statement = select(Book).where(Book.id == book_uid)
        result = await session.exec(statement)
        book = result.first()
        return book if book is not None else None

    async def create_book(self, book_data: BookCreateModel, session: AsyncSession):
        book_data_dict = book_data.model_dump()
        new_book = Book(**book_data_dict)
        session.add(new_book)
        await session.commit()
        return new_book

    async def update_book(self, book_uid: str, book_data: BookUpdateModel, session: AsyncSession):
        book_to_update = self.get_book_by_id(book_uid, session)
        if book_to_update is not None:
            book_data_dict = book_data.model_dump()
            for key, value in book_data_dict.items():
                setattr(book_to_update, key, value)

            await session.commit()
            return book_to_update
        else:
            return None

    async def delete_book(self, book_uid: str, session: AsyncSession):
        book_to_delete = self.get_book_by_id(book_uid, session)
        if book_to_delete is not None:
            await session.delete(book_to_delete)
            await session.commit()
            return book_to_delete
        else:
            return None