#!/usr/bin/env python
import fileinput

def insertion_sort(ar):
    for i, elem in enumerate(ar):
        if i == 0:
            continue
        while i != 0 and elem < ar[i - 1]:
            ar[i] = ar[i - 1]
            i -= 1
        ar[i] = elem
        yield ar


def insertionSort(ar):
    sorting = insertion_sort(ar)
    for step in sorting:
        print ' '.join([str(i) for i in step])


def main():
    input = [line.strip() for line in fileinput.input()]
    insertionSort([int(i) for i in input.pop().split()])


if __name__ == '__main__':
    main()
