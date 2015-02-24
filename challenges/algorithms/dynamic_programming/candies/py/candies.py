#!/usr/bin/env python
import fileinput


def candies(ratings):
    """ Return the minimum number of candies.
        Scan the ratings from left to right. If the current rating
        is larger than the previous, the current candies is the
        previous candies + 1. If the current rating is equal to or
        less than the previous rating, set candies to 1.
        Scan the ratings from right to left. If the current rating
        is larger than the previous, [and the current candies is
        less than the previous candies?], increment the candies.
        If the current is equal to or less than the previous,
        continue.
        :params
            ratings: list of ints representing rating per child
        :returns
            list of ints representing the number of candies per child
    """
    candies = [1 for child in range(0, len(ratings))]

    # scan left to right
    for i, rating in enumerate(ratings[1:], start=1):
        if rating > ratings[i - 1]:
            candies[i] = candies[i - 1] + 1

    # scan right to left
    for i, rating in reversed(list(enumerate(ratings[:-1]))):
        if rating > ratings[i + 1] and candies[i] <= candies[i + 1]:
            candies[i] = candies[i + 1] + 1

    return candies


def main():
    input = [line.strip() for line in fileinput.input()]

    # first line is number of test cases
    input.pop(0)

    print sum(candies(map(int, input)))


if __name__ == '__main__':
    main()
