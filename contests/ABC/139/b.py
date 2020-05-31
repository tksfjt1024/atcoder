#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


def main():
    input = stdin.buffer.readline
    a, b = map(int, input().split())

    ans = 0

    while ans * (a - 1) + 1 < b:
        ans += 1

    print(ans)


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
