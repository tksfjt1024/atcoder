#!/usr/bin/env python3

from sys import stdin, setrecursionlimit
from bisect import bisect_right


def main():
    input = stdin.buffer.readline
    n = int(input())
    v = list(map(int, input().split()))
    c = list(map(int, input().split()))

    d = [v[i] - c[i] for i in range(n)]
    d.sort()
    idx = bisect_right(d, 0)
    print(sum(d[idx:]))


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
