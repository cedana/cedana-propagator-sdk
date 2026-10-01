from enum import Enum

class CheckpointReason(str, Enum):
    Heartbeat = "heartbeat",
    Manual = "manual",
    Maintenance = "maintenance",

