import sqlalchemy as sqlalchemy
from db import metadata
from models.enums import RoleType

user = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("email", sqlalchemy.String(200), unique=True),
    sqlalchemy.Column("password", sqlalchemy.String(260)),
    sqlalchemy.Column("login", sqlalchemy.String(150)),
    sqlalchemy.Column("first_name", sqlalchemy.String(200)),
    sqlalchemy.Column("last_name", sqlalchemy.String(200)),
    sqlalchemy.Column(
        "role",
        sqlalchemy.Enum(RoleType),
        nullable=False,
    ),
)
