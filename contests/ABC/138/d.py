#!/usr/bin/env python3

from sys import stdin, setrecursionlimit
from collections import deque


def main():
    input = stdin.buffer.readline
    n, q = map(int, input().split())
    g = [[] for _ in range(n)]
    for _ in range(n - 1):
        a, b = map(int, input().split())
        g[a - 1].append(b - 1)
        g[b - 1].append(a - 1)
    counts = [0] * n
    for _ in range(q):
        p, x = map(int, input().split())
        counts[p - 1] += x

    q = deque()
    q.append(0)
    seen = [False] * n
    seen[0] = True

    while q:
        v = q.popleft()

        for n_v in g[v]:
            if seen[n_v]:
                continue
            seen[n_v] = True
            counts[n_v] += counts[v]
            q.append(n_v)

    print(*counts)


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
