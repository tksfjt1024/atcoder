#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


def main():
    input = stdin.buffer.readline
    a, b = map(int, input().split())
    if a >= 13:
        print(b)
    elif 6 <= a <= 12:
        print(b // 2)
    elif a <= 5:
        print(0)


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
