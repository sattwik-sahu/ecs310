from typing import TypeVar, List


T = TypeVar("T")


def argsort(x: List[T], reverse: bool = False) -> List[int]:
    """
    Argsort function performs the same as its counterpart in Numpy

    Args:
        x (List): The sequence to sort
        reverse (bool): Whether to return the descending order of sorted args

    Returns:
        List[int]: The list of sorted args
    """
    return sorted(range(len(x)), key=x.__getitem__)[:: (-1) ** reverse]
