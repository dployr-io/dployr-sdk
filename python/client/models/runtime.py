from enum import Enum

class Runtime(str, Enum):
    Static = "static",
    Golang = "golang",
    Php = "php",
    Python = "python",
    Nodejs = "nodejs",
    Ruby = "ruby",
    Dotnet = "dotnet",
    Java = "java",
    Docker = "docker",
    K3s = "k3s",
    Custom = "custom",

