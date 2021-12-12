from typing import Iterator


def get_commands() -> Iterator[str]:
    """
    Yields the content of the input file
    """
    with open('input', 'r') as f:
        while line := f.readline():
            yield line.strip()


def part_1():
    pos, depth = 0, 0

    for command in get_commands():
        direction, amount = command.split(' ')
        amount = int(amount)

        match direction:
            case "forward":
                pos += amount
            case "down":
                depth += amount
            case "up":
                depth -= amount

    return pos * depth


def part_2():
    pos, depth, aim = 0, 0, 0

    for command in get_commands():
        direction, amount = command.split(' ')
        amount = int(amount)

        match direction:
            case "forward":
                pos += amount
                depth += aim * amount
            case "down":
                aim += amount
            case "up":
                aim -= amount

    return pos * depth


print(part_1())
print(part_2())
