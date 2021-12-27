Lanternfish = int
Lanternfishes = list[Lanternfish]


NEWBORN_VALUE = 8
START_VALUE = 6


def get_lanternfishes() -> Lanternfishes:
    """
    Yields the content of the input file
    """
    with open('input', 'r') as f:
        return [int(x) for x in f.readline().split(',')]


def step(lanternfishes: Lanternfishes):
    """
    Goes 1 day forward
    """
    newborn = []

    for index, fish in enumerate(lanternfishes):
        if fish == 0:
            newborn.append(NEWBORN_VALUE)
            lanternfishes[index] = START_VALUE
        else:
            lanternfishes[index] = fish - 1

    lanternfishes.extend(newborn)


def part_1():
    lanternfishes: Lanternfishes = get_lanternfishes()

    for _ in range(80):
        step(lanternfishes)

    print(len(lanternfishes))


def part_2():
    lanternfishes: Lanternfishes = get_lanternfishes()

    for _ in range(256):
        step(lanternfishes)

    print(len(lanternfishes))

part_1()
part_2()
