import enum


class RoleType(enum.Enum):
    admin = "admin"
    user = "user"


class State(enum.Enum):
    created = "created"
    edited = "edited"
    deleted = "deleted"
