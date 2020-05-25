#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


def main():
    input = stdin.buffer.readline
    a, b = map(int, input().split())

    if 1 <= a <= 9 and 1 <= b <= 9:
        print(a * b)
    else:
        print(-1)


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
