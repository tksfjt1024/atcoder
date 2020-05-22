#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


def main():
    input = stdin.buffer.readline
    n = int(input())
    min = 10 ** 15
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0 and min > i + n // i - 2:
            min = i + n // i - 2
    print(min)


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
