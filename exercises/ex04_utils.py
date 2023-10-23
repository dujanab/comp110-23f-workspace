"""EX04 - List Utility Functions."""
__author__ = "730467698"


def all(input: list[int], indicated_num: int) -> int:
    """Returns True if all the numbers in the list are equal to the indicated number."""
    if len(input) == 0:
        return False
    list_idx: int = 0
    while list_idx < len(input):
        if input[list_idx] != indicated_num:
            return False
        list_idx += 1
    return True


def max(input: list[int]) -> int:
    """Returns the largest number of a given list."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    list_idx: int = 0
    max_num: int = input[0]
    while list_idx < len(input):
        if input[list_idx] > max_num:
            max_num = input[list_idx]
        list_idx += 1
    return max_num


def is_equal(input1: list[int], input2: list[int]) -> int:
    """Returns True if every element at every index is equal in both lists."""
    if len(input1) != len(input2):
        return False
    list_idx: int = 0
    while list_idx < len(input1):
        if (input1[list_idx] != input2[list_idx]):
            return False
        list_idx += 1
    return True