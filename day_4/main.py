from typing import Iterator

Board = list[list[int]]
Boards = list[Board]

def load_boards_and_extractions() -> (Boards, list[int]):
    """
    Loads boards and extractions from the input file
    """
    def parse_line(line, sep=None, cast=int) -> list:
        return [ cast(x) for x in line.strip().split(sep) ]

    with open('input', 'r') as f:
        extractions = parse_line(f.readline(), sep=',')

        boards: Boards = []

        while f.readline() and (line := f.readline()):
            boards.append([
                parse_line(line)
                for line in [line, f.readline(), f.readline(), f.readline(), f.readline()]
            ])

        return boards, extractions

def has_won(board: Board, drawn_numbers: set) -> bool:
    """
    Returns the winning row/column if the board won, otherwise None
    """
    for x in range(5):
        if all(board[x][y] in drawn_numbers for y in range(5)):
            return True
        if all(board[y][x] in drawn_numbers for y in range(5)):
            return True

    return False


def get_score(board: Board, drawn_numbers: set, last_drawn: int) -> int:
    somma = 0
    for row in board:
        for cell in row:
            if cell not in drawn_numbers:
                somma += cell

    return somma * last_drawn


def part_1():
    boards, extractions = load_boards_and_extractions()

    drawn: set = set()

    for number in extractions:
        drawn.add(number)

        winner = next((board for board in boards if has_won(board, drawn_numbers=drawn)), None)

        if winner is not None:
            return get_score(winner, drawn, number)


def part_2():
    boards_still_playing, extractions = load_boards_and_extractions()

    drawn: set = set()

    for number in extractions:
        drawn.add(number)

        old_boards = boards_still_playing
        boards_still_playing = list(board for board in boards_still_playing if not has_won(board, drawn_numbers=drawn))

        if len(boards_still_playing) == 0:
            return get_score(old_boards[0], drawn, number)


print(part_1())
print(part_2())
