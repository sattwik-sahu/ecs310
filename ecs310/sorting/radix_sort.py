from math import log
from typing import List
from ecs310.sorting import T, Sorting


class RadixSort(Sorting):
    def __init__(self) -> None:
        Sorting.__init__(self, name="counting_sort")

    def sort(self, x: List[T], reverse: bool = False) -> List[T]:
        x_maxlen = max([1 + log(i, base=10) for i in x])
        if type(x[0]) is int:
            x = [str(i).zfill(x_maxlen) for i in x]
        print()


def main():
    counting_x = [0, 3, 1, 4, 2, 7, 8, 3, 1, 4]
    counting_sort = RadixSort()
    print(counting_x, counting_sort.sort(x=counting_x), sep="\n")


if __name__ == "__main__":
    main()
