def get_crabs_x() -> list[int]:
    """
    Yields the content of the input file
    """
    with open('input', 'r') as f:
        return [int(x) for x in f.readline().split(',')]


def distance(x, y) -> int:
    return abs(x - y)

def calc_fuel_cost(positions: list[int], pos: int):
    return sum(distance(x, pos) for x in positions)

def part_1():
    positions = get_crabs_x()

    first_pos, last_pos = 0, max(positions)

    costs = [ calc_fuel_cost(positions, pos) for pos in range(first_pos, last_pos+1) ]

    print(min(costs))

part_1()
