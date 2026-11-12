from enum import Enum

class Priority(str, Enum):
    Batch = "batch",
    Standard = "standard",
    Interactive = "interactive",

