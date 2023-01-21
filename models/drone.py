import sqlalchemy as sqlalchemy
from db import metadata
from models.enums import State

drone = sqlalchemy.Table(
    "drones",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("manufacturer", sqlalchemy.String(120), nullable=False),
    sqlalchemy.Column("description", sqlalchemy.String(1000), nullable=False),
    sqlalchemy.Column("model", sqlalchemy.String(200), nullable=False),
    sqlalchemy.Column("drone_type", sqlalchemy.String(120), nullable=False),
    sqlalchemy.Column(
        "created-at",
        sqlalchemy.DateTime,
        server_default=sqlalchemy.func.now(),
    ),
    sqlalchemy.Column("photo_url", sqlalchemy.String(120), nullable=False),
    sqlalchemy.Column(
        "status",
        sqlalchemy.Enum(State),
        nullable=False,
    ),
    sqlalchemy.Column(
        "drone_pilot_id", sqlalchemy.ForeignKey("users.id"), nullable=False
    ),
)
