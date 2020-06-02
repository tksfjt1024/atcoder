#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


def main():
    input = stdin.buffer.readline
    n, d = map(int, input().split())
    ans = 0
    while ans * (2 * d + 1) < n:
        ans += 1
    print(ans)


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
