"""
https://adventofcode.com/2022/day/1
"""

from Y2022.utils import read_input


def part_one(file):
    content = read_input(file)

    cals = []
    current_cal = 0
    for i in range(len(content)):
        value = content[i].strip()

        if not value:
            cals.append(current_cal)
            current_cal = 0
        else:
            current_cal += int(value, base=10)
    cals.append(current_cal)

    return cals


def part_two(calories):
    top_three = sorted(calories, reverse=True)[:3]
    return top_three


if __name__ == "__main__":
    FILE = './input'
    TEST_FILE = 'input_test'
    cals = part_one(FILE)
    print(max(cals))
    top_three = part_two(cals)
    print(sum(top_three))
