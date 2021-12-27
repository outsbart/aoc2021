from dataclasses import dataclass
from typing import Iterator

DANGER_THRESHOLD = 2

@dataclass
class Point:
    x: int
    y: int

    def __post_init__(self):
        self.x = int(self.x)
        self.y = int(self.y)

    def __sub__(self, other):
        return Point(x=self.x - other.x, y=self.y - other.y)

    def normalized(self):
        """
        normalized-ish
        """
        def sign(num):
            if num == 0:
                return 0
            return 1 if num > 0 else -1

        return Point(x=sign(self.x), y=sign(self.y))

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self


Line = tuple[Point, Point]


def get_lines() -> Iterator[Line]:
    """
    Yields the content of the input file
    """
    with open('input', 'r') as f:
        while line := f.readline():
            points = line.strip().split(" -> ")
            yield Point(*points[0].split(',')), Point(*points[1].split(','))


def get_line_points(line: Line, exclude_diagonals=True) -> Iterator[Point]:
    """
    Yields all points in the line
    """
    x, y = line
    direction = (y - x).normalized()

    if exclude_diagonals and direction.x != 0 and direction.y != 0:
        return

    while x != y:
        yield x
        x += direction

    yield y


def draw_lines(floor, exclude_diagonals=True):
    for line in get_lines():
        for point in get_line_points(line, exclude_diagonals=exclude_diagonals):
            floor[point.x][point.y] += 1


def part_1():
    floor = [
        [0]*1000 for _ in range(1000)
    ]

    draw_lines(floor)

    return sum(1 for x in range(1000) for y in range(1000) if floor[x][y] >= DANGER_THRESHOLD)


def part_2():
    floor = [
        [0] * 1000 for _ in range(1000)
    ]

    draw_lines(floor, exclude_diagonals=False)

    return sum(1 for x in range(1000) for y in range(1000) if floor[x][y] >= DANGER_THRESHOLD)

print(part_1())
print(part_2())
