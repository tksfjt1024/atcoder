#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


def main():
    input = stdin.buffer.readline
    n = int(input())

    for i in range(1, 10):
        if n % i == 0 and 1 <= n // i <= 9:
            print('Yes')
            exit()
    print('No')


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
