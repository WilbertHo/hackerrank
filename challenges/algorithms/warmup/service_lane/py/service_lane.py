#!/usr/bin/python

import fileinput

def main():
    # read input
    _input = [line.strip() for line in fileinput.input()]

    # first line: length of road, num test cases
    _input.pop(0)
    # second line: array representing road
    road = [int(width) for width in _input.pop(0).split()]

    for case in _input:
        enter, exit = [int(width) for width in case.split()]
        exit += 1
        print min(road[enter:exit])

if __name__ == '__main__':
    main()
