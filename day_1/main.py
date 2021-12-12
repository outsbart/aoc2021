from itertools import pairwise
from typing import Iterator


def get_depth_measurements() -> Iterator[int]:
    """
    Yields the content of the input file
    """
    with open('input', 'r') as f:
        while line := f.readline():
            yield int(line.strip())


def triplewise(iterable):
    """
    Return overlapping triplets from an iterable
    eg: triplewise('ABCDEFG') -> ABC BCD CDE DEF EFG
    """
    for (a, _), (b, c) in pairwise(pairwise(iterable)):
        yield a, b, c


def count_consecutives_increases(iterable):
    return sum(d2 > d1 for d1, d2 in pairwise(iterable))


part_1 = count_consecutives_increases(get_depth_measurements())

print(part_1)


part_2 = count_consecutives_increases(map(sum, triplewise(get_depth_measurements())))

print(part_2)
