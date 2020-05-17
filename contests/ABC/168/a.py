#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


def main():
    input = stdin.buffer.readline
    n = input()[:-1].decode()
    last = int(n[-1])
    if last == 2 or last == 4 or last == 5 or last == 7 or last == 9:
        print('hon')
    elif last == 0 or last == 1 or last == 6 or last == 8:
        print('pon')
    elif last == 3:
        print('bon')


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
