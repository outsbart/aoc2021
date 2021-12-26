import operator
from collections import defaultdict
from typing import Iterator

gamma_rate = int
epsilon_rate = int

def get_diagnostics() -> Iterator[str]:
    """
    Yields the content of the input file
    """
    with open('input', 'r') as f:
        while line := f.readline():
            yield line.strip()


def calc_power_rates(diagnostics) -> (gamma_rate, epsilon_rate):
    sums: dict[int, int] = defaultdict(int)
    count: int = 0

    for count, value in enumerate(diagnostics):
        for index, bit in enumerate(value):
            sums[index] += int(bit)

    binary = ''
    for index, somma in sums.items():
        binary += str(int(somma > count/2))

    gamma = int(binary, 2)
    return gamma, gamma ^ int('1' * len(sums), 2)


def most_common_value(numbers: list[str], position=0, func=operator.ge) -> str:
    """
    Determines the most common value in a given position for all given numbers
    Returns '0' or '1'
    """
    return str(
        int(
            func(
                sum(int(number[position]) for number in numbers),
                len(numbers)/2
            )
        )
    )


def get_rating(func) -> int:
    diagnostics = list(get_diagnostics())
    position = 0

    while len(diagnostics) > 1:
        value = most_common_value(diagnostics, position=position, func=func)
        diagnostics = [ d for d in diagnostics if d[position] == value ]
        position += 1

    return int(diagnostics[0], 2)


def get_oxygen_generator_rating() -> int:
    return get_rating(func=operator.ge)


def get_co2_scrubber_rating() -> int:
    return get_rating(func=operator.lt)


g, e = calc_power_rates(get_diagnostics())

part_1 = g * e
print(part_1)


oxygen = get_oxygen_generator_rating()
co2 = get_co2_scrubber_rating()

print(oxygen * co2)
