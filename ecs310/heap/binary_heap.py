from random import randint
from ecs310.heap import Heap, HeapNode


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
                print(f"switching {p_node} and {node}")
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
            c_inx, c_node = self._get_children(inx)[0]
            if c_node is not None:
                print(f"Found child of {self.nodes[inx]} - {c_node}")
                if (self.nodes[inx] <= c_node) == self.is_max_heap:
                    print(f"Switching {self.nodes[inx]} and {c_node}")
                    self.nodes[c_inx], self.nodes[inx] = (
                        self.nodes[inx],
                        self.nodes[c_inx],
                    )
                    inx = c_inx
                else:
                    break
            else:
                break

        return pop_node


h = BinaryHeap()
for i in range(10):
    h.insert(HeapNode(value=randint(-10, 10)))
    print(h.nodes)

for i in range(10):
    print(h.pop())
