import typing as t

from pydantic import BaseModel
from tortoise.contrib.pydantic import pydantic_model_creator

from apps.blog.models import Author
from apps.blog.models import Blog


class AuthorCreateInput(BaseModel):
    """
    Create Author Input
    """

    name: str


class AuthorPartialUpdateInput(BaseModel):
    """
    Partial Update Author Input
    """

    name: t.Optional[str] = None


class AuthorUpdateInput(BaseModel):
    """
    Update Author Input
    """

    name: str


AuthorOutput = pydantic_model_creator(Author, name="AuthorOutput", exclude=("deleted_at",))


class BlogCreateInput(BaseModel):
    """
    Create Blog Input
    """

    author_id: int
    title: str
    content: str
    published: bool = False


class BlogPartialUpdateInput(BaseModel):
    """
    Partial Update Blog Input
    """

    title: t.Optional[str] = None
    content: t.Optional[str] = None
    published: t.Optional[bool] = None


class BlogUpdateInput(BaseModel):
    """
    Update Blog Input
    """

    title: str
    content: str
    published: bool


BlogOutput = pydantic_model_creator(Blog, name="BlogOutput", exclude=("deleted_at",), optional=("published_at",))
