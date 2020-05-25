#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


def main():
    input = stdin.buffer.readline
    n = int(input())

    i = int(n ** 0.5)

    while i >= 1:
        if n % i == 0:
            j = n // i
            print(i + n // i - 2)
            exit()
        i -= 1


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
