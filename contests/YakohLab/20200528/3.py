#!/usr/bin/env python3

from sys import stdin, setrecursionlimit
from bisect import bisect_left


def main():
    input = stdin.buffer.readline
    n, m = map(int, input().split())
    py = [list(map(int, input().split())) for _ in range(m)]

    summary = [[] for _ in range(n)]

    for p, y in py:
        summary[p - 1].append(y)

    for i in range(n):
        summary[i].sort()

    for p, y in py:
        print(str(p).zfill(6), str(bisect_left(summary[p - 1], y) + 1).zfill(6), sep='')


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
