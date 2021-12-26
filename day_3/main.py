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


g, e = calc_power_rates(get_diagnostics())

part_1 = g * e
print(part_1)
