from datetime import datetime

from tortoise import fields

from core.tortoise.models import BaseModel


class Author(BaseModel):
    name: str = fields.CharField(max_length=255)


class Blog(BaseModel):
    title: str = fields.CharField(max_length=255)
    content: str = fields.TextField()
    author = fields.ForeignKeyField("models.Author", related_name="blogs")

    views: int = fields.IntField(default=0)
    likes: int = fields.IntField(default=0)
    published: bool = fields.BooleanField(default=False)
    published_at: datetime = fields.DatetimeField(null=True)
