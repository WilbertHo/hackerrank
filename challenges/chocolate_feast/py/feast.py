#!/usr/bin/env python

def main():
    credit = 10
    cost = 2
    total = 0

    while(credit >= cost):
        total += credit / cost
        leftover = (credit / cost) + (credit % cost)
        credit = leftover

    print total

if __name__ == '__main__':
    main()
