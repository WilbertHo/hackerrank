#!/usr/bin/env python

import fileinput


def main():
    input = [line.strip() for line in fileinput.input()]

    num_cases = input.pop(0)
    gems = set(input[0])

    for rock in input:
        elements = set()
        for element in rock:
            elements.add(element)
        gems = gems.intersection(elements)

    print len(gems)


if __name__ == '__main__':
    main()
