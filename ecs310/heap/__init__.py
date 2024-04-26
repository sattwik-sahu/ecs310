from abc import ABC, abstractmethod
from typing import List, TypeVar, Tuple


TValue = TypeVar("TValue", int, float)


class HeapNode(ABC):
    def __init__(self, value: TValue, id: int | str | None = None) -> None:
        self.id = id
        self.value = value

    def __repr__(self) -> TValue:
        return self.value

    def __str__(self) -> str:
        return f"<{self.value}>"

    def __repr__(self) -> str:
        return str(self)

    def __eq__(self, value: TValue) -> bool:
        return self.value == value

    def __lt__(self, value: TValue) -> bool:
        return self.value < value

    def __le__(self, value: TValue) -> bool:
        return self.value <= value

    def __gt__(self, value: TValue) -> bool:
        return self.value > value

    def __ge__(self, value: TValue) -> bool:
        return self.value >= value


class Heap(ABC):
    name: str
    nodes: List[HeapNode]

    def __init__(self, name: str, n_children_per_node: int) -> None:
        self.name = name
        self.n_children_per_node = n_children_per_node
        self.nodes = []

    def _get_parent(self, inx: int) -> HeapNode:
        parent_inx = inx // 2
        parent = self.nodes[parent_inx]

        return parent_inx, parent

    def _get_children(self, inx: int) -> Tuple[Tuple[int, HeapNode]]:
        children: List[Tuple[int, HeapNode]] = []
        for i in range(self.n_children_per_node):
            c_inx = (inx * self.n_children_per_node) + (i + 1)
            if c_inx < len(self.nodes):
                children.append((c_inx, self.nodes[c_inx]))

        return tuple(children)

    @abstractmethod
    def insert(self, node: HeapNode) -> int:
        pass

    @abstractmethod
    def pop(self) -> HeapNode:
        pass
