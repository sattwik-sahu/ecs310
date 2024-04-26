from ftplib import MAXLINE
from math import log
from random import randint
from typing import List, Type
from ecs310.sorting import T, Sorting
from ecs310.sorting.counting_sort import CountingSort


def extract_digit(num: int, inx: int) -> int:
    p = (num // (10**inx)) % 10
    return p


class RadixSort(Sorting):
    def __init__(self) -> None:
        Sorting.__init__(self, name="counting_sort")

    def sort(self, x: List[int], reverse: bool = False) -> List[int]:
        x_maxlen = int(log(max(x)) / log(10)) + 1

        counting_sort = CountingSort()
        x_sorted = x.copy()
        for i in range(x_maxlen):
            x_ = x_sorted.copy()
            x_sorted.clear()
            digits_sorted = counting_sort.sort(
                list(set([extract_digit(v, i) for v in x_]))
            )
            for sorted_digit in digits_sorted:
                x_sorted.extend([j for j in x_ if extract_digit(j, i) == sorted_digit])

        return x_sorted[:: (-1) ** reverse]


def main():
    counting_x = [randint(0, 10000) for i in range(10)]
    counting_sort = RadixSort()
    print(counting_x, counting_sort.sort(x=counting_x), sep="\n")


if __name__ == "__main__":
    main()
