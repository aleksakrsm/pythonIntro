from typing import Optional, List
from sqlmodel import SQLModel, Field, Relationship

class AuthorBook(SQLModel, table=True):
    author_id: Optional[int] = Field(default=None, foreign_key="author.id", primary_key=True)
    book_id: Optional[int] = Field(default=None, foreign_key="book.id", primary_key=True)

# Define Author Model
class Author(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str

    books: List["Book"] = Relationship(back_populates="authors", link_model=AuthorBook)

# Define Book Model
class Book(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str

    authors: List[Author] = Relationship(back_populates="books", link_model=AuthorBook)

