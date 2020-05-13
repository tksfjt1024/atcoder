#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


def main():
    input = stdin.buffer.readline
    a, b, k = map(int, input().split())
    if a >= k:
        print(a - k, b)
    elif a < k <= a + b:
        print(0, a + b - k)
    else:
        print(0, 0)


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
