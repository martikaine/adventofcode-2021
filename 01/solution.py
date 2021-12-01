from typing import List


def parse_depths() -> List[int]:
    with open('input.txt', 'r') as f:
        return [int(line.strip()) for line in f.readlines()]


def solve_part_one(depths):
    increases = 0
    previous = None

    for value in depths:
        if previous is not None and value > previous:
            increases += 1

        previous = value

    print(f'Part one: {increases}')


def solve_part_two(depths):
    increases = 0
    previous = None

    for i in range(0, len(depths)-2):
        current = sum(depths[i:i+3])

        if previous is not None and current > previous:
            increases += 1

        previous = current

    print(f'Part two: {increases}')


depths = parse_depths()
solve_part_one(depths)
solve_part_two(depths)
