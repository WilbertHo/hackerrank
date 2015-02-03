#!/usr/bin/env python
import fileinput


def partition(ar, low, high):
    small_end = low
    pivot = ar[high]

    i = low
    while i <= high:
    # for i in range(low, high):
    # for i, elem in enumerate(ar):
        elem = ar[i]
        if elem <= pivot:
            # swap the element being examined with the
            # end of the subarray
            ar[i], ar[small_end] = ar[small_end], ar[i]
            small_end += 1

        i+= 1

    # return the index of the pivot
    return small_end - 1


def quicksort(ar, low=None, high=None):
    """ In-place quicksort. """
    if low is None:
        low = 0

    if high is None:
        high = len(ar) - 1

    if low < high:
        pivot = partition(ar, low, high)
        quicksort(ar, low, pivot - 1)
        quicksort(ar, pivot + 1, high)

    return ar


def main():
    input = [line.strip() for line in fileinput.input()]
    ar = map(int, input[-1].split())
    print quicksort(ar)


if __name__ == '__main__':
    main()
