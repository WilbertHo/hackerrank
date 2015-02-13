#!/usr/bin/env python
import fileinput
from itertools import permutations


def get_count(nums):
    count = 0
    for i, j in permutations(range(0, len(nums)), 2):
        if i == j:
            continue
        if nums[i] == nums[j]:
            count += 1

    return count


def main():
    input = [line.strip() for line in fileinput.input()]
    input.pop(0)
    for i in range(1, len(input) + 1, 2):
        nums = input[i]
        print get_count(map(int, nums.split()))


if __name__ == '__main__':
    main()
