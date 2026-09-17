from enum import Enum

class LifetimeState(str, Enum):
    Heartbeat = "heartbeat",
    Finished = "finished",
    Cancelled = "cancelled",

