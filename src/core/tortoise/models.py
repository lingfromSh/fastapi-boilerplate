from datetime import datetime

from tortoise import Model
from tortoise import fields
from tortoise.manager import Manager


class AliveManager(Manager):
    def get_queryset(self):
        return super().get_queryset().filter(deleted_at=0)


class DeadManager(Manager):
    def get_queryset(self):
        return super().get_queryset().exclude(deleted_at=0)


class BaseModel(Model):
    id: int = fields.BigIntField(pk=True)

    created_at: datetime = fields.DatetimeField(auto_now_add=True)
    updated_at: datetime = fields.DatetimeField(auto_now=True)
    deleted_at: int = fields.BigIntField(default=0, db_index=True)

    alive_objects = AliveManager()
    dead_objects = DeadManager()

    class Meta:
        abstract = True
