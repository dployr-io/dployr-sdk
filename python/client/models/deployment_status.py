from enum import Enum

class DeploymentStatus(str, Enum):
    Pending = "pending",
    In_progress = "in_progress",
    Failed = "failed",
    Completed = "completed",

