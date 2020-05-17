#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


def main():
    input = stdin.buffer.readline
    a, b, n = map(int, input().split())

    x = min(b - 1, n)

    print(int(a * x / b) - a * int(x / b))


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
