from enum import Enum

class Source(str, Enum):
    Profile = "profile",
    Team = "team",
    Org = "org",
    Default = "default",

