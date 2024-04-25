from typing import List, TypeVar, Dict
from abc import ABC, abstractmethod


T = TypeVar("T")


class Sorting(ABC):
    def __init__(self, name: str, *args, **kwargs) -> None:
        self.name = name

    @abstractmethod
    def sort(self, x: List[T], reverse: bool = False) -> List[T]:
        pass
