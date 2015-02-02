#!/usr/bin/env python
import fileinput


def quicksort(ar):
    pass


def main():
    input = [line.strip() for line in fileinput.input()]
    print quicksort(map(int, input[-1]))


if __name__ == '__main__':
    main()
