#!/usr/bin/env python
import fileinput
import math


def maximize(l, r):
    """ Return the maximum value of A XOR B, where L <= A <= B <= R

        log2 of n is the number of times n has to be divided
        by 2 to be less than or equal to 1, so it can tell us where
        the most significant bit is.
        ex: int(log2(1)) == 0 meaning 2 ** 0
            int(log2(10)) == 3 (1010) 2 ** 3 + 2 ** 1
            int(log2(8)) == 3 (1000) 2 ** 3

        Test case: 10, 15 -> 7
        10: 1010, 15: 1111
        10 ^ 15 == 5, or 1010 ^ 1111 == 0101
        The most significant bit of 1010 and 1111 are both 1, so
        the range between 1010 to 1111 will have a max of 111.

        Test case: 1, 10 -> 15
        1: 0001, 10: 1010
        1 ^ 10 == 11, ie 0001 ^ 1010 == 1111

        The log2 will give the position of the most significant bit
        of L ^ R.
        math.log(10 ^ 15, 2) == 2.3219...
        10 ^ 15 == 5 (0101) or (2 ** 2, with the rest being 2 ** 0)
        Having the most significant bit, we can calculate the max by
        setting all bits smaller than the most significant to 1.
        We'll do that by finding the most significant bit's next larger
        and subtracting 1 from that.
        int(math.ceil(math.log(10 ^ 15, 2))) == 3
        and 2 ** 3 == 8
        8 - 1 == 7 (0111)
    """
    return 2 ** int(math.ceil(math.log(l ^ r, 2))) - 1


def main():
    input = [line.strip() for line in fileinput.input()]
    print maximize(*map(int, input))


if __name__ == '__main__':
    main()
