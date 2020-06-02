#!/usr/bin/env python3

from sys import stdin, setrecursionlimit
from collections import defaultdict
from heapq import heapify, heappush, heappushpop


def main():
    input = stdin.buffer.readline
    n, m = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(n)]

    dic = defaultdict(list)
    for a, b in ab:
        dic[a].append(b)

    q = []
    heapify(q)

    for i in sorted(dic.keys(), reverse=True):
        for j in sorted(dic[i], reverse=True):
            if len(q) <= m - i:
                heappush(q, j)
            elif q and q[0] < j:
                heappushpop(q, j)

    print(sum(q))


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
