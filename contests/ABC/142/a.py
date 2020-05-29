#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


def main():
    input = stdin.buffer.readline
    n = int(input())
    if n % 2 == 0:
        print(1 / 2)
    else:
        print((n // 2 + 1) / n)


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
