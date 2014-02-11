#!/usr/bin/env python

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
    # Total candies == credit/cost + wrappers/wrapper_cost
    credit = 10
    cost = 2
    wrapper_cost = 5

    print calcCandies(credit, cost, wrapper_cost)

    print calcCandies(12, 4, 4)
    print calcCandies(6, 2, 2)

if __name__ == '__main__':
    main()
