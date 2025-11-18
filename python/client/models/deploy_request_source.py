from enum import Enum

class DeployRequest_source(str, Enum):
    Remote = "remote",
    Image = "image",

