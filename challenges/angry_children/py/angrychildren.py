#!/usr/bin/python

import fileinput

def main():
    # read the input
    input = [int(line.strip()) for line in fileinput.input()]
    input_size = input.pop(0)
    window_size = input.pop(0)

    # sort the input
    input = sorted(input)

    # sliding window
    win_start = 0
    win_end = window_size - 1
    mininum = input[-1] - input[0]

    while (win_end < len(input)):
        window_min = input[win_end] - input[win_start]
        mininum = window_min if window_min < mininum else mininum
        win_start += 1
        win_end += 1

    # print result
    print mininum

if __name__ == '__main__':
    main()
