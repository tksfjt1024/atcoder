#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


def main():
    input = stdin.buffer.readline
    a, b = map(int, input().split())
    ans = a - 2 * b
    if ans >= 0:
        print(ans)
    else:
        print(0)


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
