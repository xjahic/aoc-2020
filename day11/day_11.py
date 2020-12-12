import copy
import functools
import operator


def count_occupied_seats(seating_area: list):
    # flatten then count
    return functools.reduce(operator.iconcat, seating_area, []).count("#")


def count_occupied_adjacent_seats(seating_area, row, column):
    occupied = 0
    for r in range(row - 1, row + 2):  # row -1, row, row + 1
        for c in range(column - 1, column + 2):  # column - 1, column, column + 1
            if r == row and c == column:
                # not adjacent
                continue
            elif r < 0 or r == len(seating_area) or c < 0 or c == len(seating_area[0]):
                # out of range
                continue
            elif seating_area[r][c] == "#":
                # adjacent is occupied
                occupied += 1
    return occupied


def apply_rules(seating_area: list):
    new_seating_area = copy.deepcopy(seating_area)
    for row in range(len(seating_area)):
        for column in range(len(seating_area[0])):
            occupied_adjacent = count_occupied_adjacent_seats(seating_area, row, column)
            if seating_area[row][column] == "L" and occupied_adjacent == 0:
                new_seating_area[row][column] = "#"
            elif seating_area[row][column] == "#" and occupied_adjacent >= 4:
                new_seating_area[row][column] = "L"
    return new_seating_area


def read_input():
    return [[c for c in line.rstrip()] for line in open("input.txt")]


def part_1(seating_area: list):
    previously_occupied = count_occupied_seats(seating_area)
    while True:
        seating_area = apply_rules(seating_area)
        occupied_after_rules = count_occupied_seats(seating_area)
        if occupied_after_rules == previously_occupied:
            print(occupied_after_rules)
            break
        previously_occupied = occupied_after_rules


part_1(read_input())  # part
