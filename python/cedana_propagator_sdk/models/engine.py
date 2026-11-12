from enum import Enum

class Engine(str, Enum):
    Sglang = "sglang",
    Vllm = "vllm",

