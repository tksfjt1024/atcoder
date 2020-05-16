#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


def main():
    input = stdin.buffer.readline
    n, x, y = map(int, input().split())
    ans = [0] * (n - 1)
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            d = min(j - i, abs(i - x) + abs(j - y) + 1, abs(i - y) + abs(j - x) + 1)
            ans[d - 1] += 1
    print(*ans, sep='\n')


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
