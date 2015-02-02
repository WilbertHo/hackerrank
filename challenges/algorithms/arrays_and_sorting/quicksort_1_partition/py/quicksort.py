import fileinput


def partition(ar):
    less_than = list()
    greater_than = list()
    pivot = ar[0]

    for elem in ar[1:]:
        (less_than if elem < pivot else greater_than).append(elem)

    return less_than + [pivot] + greater_than


def main():
    input = [line.strip() for line in fileinput.input()]
    print ' '.join(map(str, partition(map(int, input[-1].split()))))


if __name__ == '__main__':
    main()
