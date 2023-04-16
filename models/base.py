# pylint: disable=missing-docstring

from sqlalchemy import inspect
from initializer import db


class Base(db.Model):
    __abstract__ = True

    def to_dict(self) -> dict:
        return { c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs}
