from enum import Enum

class ApiKind(str, Enum):
    Openai_chat = "openai_chat",
    Http = "http",

