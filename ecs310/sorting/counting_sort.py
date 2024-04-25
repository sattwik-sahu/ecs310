from typing import List
from ecs310.sorting import T, Sorting


class CountingSort(Sorting):
    def __init__(self) -> None:
        Sorting.__init__(self, name="counting_sort")

    def sort(self, x: List[T], reverse: bool = False) -> List[T]:
        x_min = min(x)
        freqs = [0] * (max(x) - min(x) + 1)
        for i in x:
            freqs[i - x_min] += 1

        x_sorted: List[T] = []
        for i, v in enumerate(freqs):
            x_sorted.extend([i - x_min] * v)

        return x_sorted[:: (-1) ** reverse]


def main():
    counting_x = [0, 3, 1, 4, 2, 7, 8, 3, 1, 4]
    counting_sort = CountingSort()
    print(counting_x, counting_sort.sort(x=counting_x), sep="\n")


if __name__ == "__main__":
    main()
