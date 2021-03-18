from dataclasses import dataclass
from typing import Union
from typing import List

@dataclass
class Metadata:
    __slots__ = ["deez", "nuts"]
    deez    : str
    nuts    : str
