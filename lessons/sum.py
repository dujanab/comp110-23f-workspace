"""Summing the elements of a list using different loops."""
__author__ = "730467698"


def w_sum(vals: list[float]) -> float:
    """Using a while loop to determnine sum of list."""
    idx: int = 0
    sum_num: float = 0.0
    while idx < len(vals):
        sum_num += vals[idx]
        idx += 1
    return sum_num


def f_sum(vals: list[float]) -> float:
    """Using a for...in... loop to determnine sum of list."""
    sum_num: float = 0.0
    for elem in vals:
        sum_num += elem
    return sum_num


def f_range_sum(vals: list[float]) -> float:
    """Using a for...in...range to determnine sum of list."""
    idx: int = 0
    sum_num: float = 0.0
    max_elem: int = len(vals)
    for idx in range(0, max_elem):
        sum_num += vals[idx]
    return sum_num