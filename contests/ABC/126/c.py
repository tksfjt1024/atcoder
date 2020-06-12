#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


def main():
    input = stdin.buffer.readline
    n, k = map(int, input().split())
    ans = 0.0

    for i in range(1, n + 1):
        tmp = 1 / n
        while i <= k - 1:
            tmp *= 0.5
            i *= 2
        ans += tmp

    print(ans)


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
