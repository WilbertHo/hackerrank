#!/usr/bin/env python

import fileinput


def calc_height(cycles):
    height = 1  # height starts at 1 for cycles = 0
    for i in range(1, cycles + 1):
        if i % 2 == 0:
            height += 1
        else:
            height = height * 2

    return height


def main():
    input = [int(line.strip()) for line in fileinput.input()]

    for i in input[1:]:
        print calc_height(i)


if __name__ == '__main__':
    main()
