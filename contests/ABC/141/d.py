#!/usr/bin/env python3

from sys import stdin, setrecursionlimit
from heapq import heapify, heappop, heappush


def main():
    input = stdin.buffer.readline
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a = [-ai for ai in a]
    heapify(a)

    for _ in range(m):
        tmp = -heappop(a)
        heappush(a, -(tmp // 2))

    print(-sum(a))


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
