#!/usr/bin/env python3

from sys import stdin, setrecursionlimit
from collections import deque


def main():
    input = stdin.buffer.readline
    n = int(input())
    g = [int(input()) - 1 for _ in range(n)]
    q = deque([0])
    seen = [-1] * n
    seen[0] = 0

    while q:
        u = q.popleft()
        v = g[u]
        if seen[v] == -1 or seen[v] > seen[u] + 1:
            seen[v] = seen[u] + 1
            q.append(v)

    print(seen[1])


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
