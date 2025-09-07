from pydantic import BaseModel
import uuid
from datetime import datetime

class Book(BaseModel):
    id: uuid.UUID
    title: str
    author: str
    year: int
    create_at : datetime
    update_at : datetime

class BookCreateModel(BaseModel):
    title: str
    author: str
    year: int
    
class BookUpdateModel(BaseModel):
    title: str
    author: str
    year: int