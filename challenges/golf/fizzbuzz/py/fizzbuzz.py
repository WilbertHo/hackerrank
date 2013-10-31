#!/usr/bin/python


def main():
    for i in range(1, 101):
        print ('Fizz' if not i % 3 else '') + ('Buzz' if not i % 5 else '') or i

if __name__ == '__main__':
    main()
