"""
https://adventofcode.com/2022/day/2
"""

from Y2022.utils import read_input

rock = 1
paper = 2
scissors = 3

loss = 0
draw = 3
win = 6


def part_one(file):
    content = read_input(file)

    combinations = {
        # opponent chose rock
        'A X': rock + draw,
        'A Y': paper + win,
        'A Z': scissors + loss,
        # opponent chose paper
        'B X': rock + loss,
        'B Y': paper + draw,
        'B Z': scissors + win,
        # opponent chose scissors
        'C X': rock + win,
        'C Y': paper + loss,
        'C Z': scissors + draw
    }

    scores = [combinations[r.strip()] for r in content]

    return sum(scores)


def part_two(file):
    content = read_input(file)

    combinations = {
        # opponent chose rock
        'A X': scissors + loss,
        'A Y': rock + draw,
        'A Z': paper + win,
        # opponent chose paper
        'B X': rock + loss,
        'B Y': paper + draw,
        'B Z': scissors + win,
        # opponent chose scissors
        'C X': paper + loss,
        'C Y': scissors + draw,
        'C Z': rock + win
    }

    scores = [combinations[r.strip()] for r in content]

    return sum(scores)


if __name__ == "__main__":
    FILE = './input'
    total_score = part_one(FILE)
    print(total_score)
    total_score = part_two(FILE)
    print(total_score)
