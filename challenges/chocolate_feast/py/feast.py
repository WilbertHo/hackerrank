#!/usr/bin/env python
import fileinput

def calcCandies(credit, cost, wrapper_cost):
    total = (credit / cost)

    credit = (credit / cost)
    cost = wrapper_cost
    while(credit >= cost):
        total += credit / cost
        leftover = (credit / cost) + (credit % cost)
        credit = leftover

    return total

def main():
    input = [line.strip() for line in fileinput.input()]

    # numCases is the first line
    numCases = input.pop(0)

    # Total candies == credit/cost + wrappers/wrapper_cost
    for line in input:
        credit, cost, wrapper_cost = [int(x) for x in line.split()]
        print calcCandies(credit, cost, wrapper_cost)

if __name__ == '__main__':
    main()
