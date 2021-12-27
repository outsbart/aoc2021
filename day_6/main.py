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

    # grouped by days left before a new fish is created
    counter = [0] * (NEWBORN_VALUE + 1)

    for fish in lanternfishes:
        counter[fish] += 1

    for _ in range(256):
        # todo: Do it in-place?
        new_counter = [0] * (NEWBORN_VALUE + 1)

        for days_left, fish_count in enumerate(counter):
            if days_left == 0:
                new_counter[NEWBORN_VALUE] += fish_count
                new_counter[START_VALUE] += fish_count
            else:
                new_counter[days_left - 1] += fish_count

        counter = new_counter

    print(sum(counter))


part_1()
part_2()
