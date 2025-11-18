from enum import Enum

class Role(str, Enum):
    Owner = "owner",
    Admin = "admin",
    Developer = "developer",
    Viewer = "viewer",

