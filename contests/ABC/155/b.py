#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


def main():
    n = int(stdin.readline())
    a = list(map(int, stdin.readline().split()))

    for ai in a:
        if ai % 2 == 0 and ai % 3 != 0 and ai % 5 != 0:
            print('DENIED')
            exit()
    print('APPROVED')


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
