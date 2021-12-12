from itertools import pairwise
from typing import Iterator


def get_depth_measurements() -> Iterator[int]:
    """
    Yields the content of the input file
    """
    with open('input', 'r') as f:
        while line := f.readline():
            yield line


total = sum(d2 > d1 for d1, d2 in pairwise(get_depth_measurements()))

print(total)
