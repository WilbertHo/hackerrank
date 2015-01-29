#!/usr/bin/env python
import fileinput

def insertion_sort(unsorted):
    for i, elem in enumerate(unsorted):
        while i != 0 and elem < unsorted[i - 1]:
            unsorted[i] = unsorted[i - 1]
            i -= 1
            yield unsorted
        if elem < unsorted[i]:
            unsorted[i] = elem
            yield unsorted


def insertionSort(ar):
    sorting = insertion_sort(ar)
    for step in sorting:
        print ' '.join([str(i) for i in step])


def main():
    input = [line.strip() for line in fileinput.input()]
    insertionSort([int(i) for i in input.pop().split()])


if __name__ == '__main__':
    main()
