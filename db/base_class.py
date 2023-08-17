from typing import Any
from sqlalchemy.ext.declarative import as_declarative, declared_attr


@as_declarative()
class Base:
    id: Any
    __name__: str

    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()

    def dict(self):
        return {c.name: getattr(self, c.name, None) for c in self.__table__.columns}

    def list(self):
        return [getattr(self, c.name, None) for c in self.__table__.columns]
