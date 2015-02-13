from collections import defaultdict
import fileinput


def closest_numbers(ar):
    sorted_ar = sorted(ar)
    closest_pairs = list()
    minimum = sorted_ar[-1] - sorted_ar[0]
    for i, j in zip(range(0, len(sorted_ar) - 1),
                    range(1, len(sorted_ar))):
        difference = sorted_ar[j] - sorted_ar[i]
        if difference < minimum:
            closest_pairs = list()
            minimum = difference
        if difference == minimum:
            closest_pairs.extend((sorted_ar[i], sorted_ar[j]))

    return closest_pairs


def main():
    input = [line.strip() for line in fileinput.input()]
    # don't need the first line
    input.pop(0)

    # print ' '.join(closest_numbers(input))
    closest_pairs = closest_numbers(map(int, input.pop().split()))
    print ' '.join(map(str, closest_pairs))


if __name__ == '__main__':
    main()
