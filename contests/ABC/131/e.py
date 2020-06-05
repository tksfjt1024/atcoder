#!/usr/bin/env python3

from sys import stdin, setrecursionlimit
from collections import deque


def main():
    INF = float('inf')
    input = stdin.buffer.readline
    n, k = map(int, input().split())
    if k > (n - 1) * (n - 2) // 2:
        print(-1)
    else:
        ab = [[i, j] for i in range(1, n) for j in range(i + 1, n + 1)]
        m = n - 1 + (n - 1) * (n - 2) // 2 - k
        print(m)
        for i, j in ab[:m]:
            print(i, j)


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
