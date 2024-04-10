from sqlalchemy import (
    MetaData,
    Table,
    Column,
    Integer,
    String,
    TIMESTAMP,
    Text,
    ForeignKey,
    func,
)
from src.auth.models import user

metadata = MetaData()

note = Table(
    "note",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("title", String(255), nullable=False),
    Column("content", Text, nullable=True),
    Column("user_id", Integer, ForeignKey(user.c.id), nullable=False),
    Column("created_at", TIMESTAMP, default=func.now()),
    Column("updated_at", TIMESTAMP, default=func.now(), onupdate=func.now()),
)
