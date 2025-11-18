from enum import Enum

class SystemStatus_status(str, Enum):
    Healthy = "healthy",
    Degraded = "degraded",
    Unhealthy = "unhealthy",

