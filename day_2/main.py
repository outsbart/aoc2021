from typing import Iterator


def get_commands() -> Iterator[str]:
    """
    Yields the content of the input file
    """
    with open('input', 'r') as f:
        while line := f.readline():
            yield line.strip()


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

print(pos * depth)
