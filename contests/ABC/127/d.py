#!/usr/bin/env python3

from sys import stdin, setrecursionlimit
from heapq import heapify, heappop, heappush


def main():
    input = stdin.buffer.readline
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    bc = [list(map(int, input().split())) for _ in range(m)]
    bc.sort(key=lambda x: -x[1])
    heapify(a)

    for i in range(m):
        b, c = bc[i]
        for _ in range(b):
            ai = heappop(a)
            if ai < c:
                heappush(a, c)
            else:
                heappush(a, ai)
                break

    print(sum(a))


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
