#!/usr/bin/env python3

from sys import stdin, setrecursionlimit
from heapq import heapify, heappop, heappush


def main():
    input = stdin.buffer.readline
    n = int(input())
    v = list(map(int, input().split()))
    heapify(v)

    for _ in range(n - 1):
        x = heappop(v)
        y = heappop(v)
        heappush(v, (x + y) / 2)

    print(v[0])


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
