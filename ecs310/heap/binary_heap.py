from random import randint
from ecs310.heap import Heap, HeapNode
from ecs310.sorting.utils import argsort


class BinaryHeap(Heap):
    def __init__(self, is_max_heap: bool = False) -> None:
        super().__init__(name="binary_heap", n_children_per_node=2)
        self.is_max_heap = is_max_heap

    def insert(self, node: HeapNode) -> int:
        insert_inx = len(self.nodes)
        self.nodes.append(node)
        while True:
            p_inx, p_node = self._get_parent(insert_inx)
            if (node >= p_node) == self.is_max_heap:
                self.nodes[p_inx], self.nodes[insert_inx] = (
                    self.nodes[insert_inx],
                    self.nodes[p_inx],
                )
                insert_inx = p_inx
            else:
                break

        return insert_inx

    def pop(self) -> HeapNode:
        pop_node = self.nodes[0]
        self.nodes[0], self.nodes[-1] = self.nodes[-1], self.nodes[0]
        self.nodes = self.nodes[:-1]

        inx = 0
        while True:
            children = self._get_children(inx)

            if len(children) == 0:
                break
            swap_inx = children[
                argsort([c[1] for c in children], reverse=self.is_max_heap)[0]
            ][0]
            if (self.nodes[swap_inx] >= self.nodes[inx]) == self.is_max_heap:
                self.nodes[inx], self.nodes[swap_inx] = (
                    self.nodes[swap_inx],
                    self.nodes[inx],
                )
                inx = swap_inx
            else:
                break

        return pop_node


h = BinaryHeap(is_max_heap=False)
for i in range(10):
    h.insert(HeapNode(value=randint(-10, 10)))
    print(h.nodes)

for i in range(10):
    print(h.pop())
