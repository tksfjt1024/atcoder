#!/usr/bin/env python3

from sys import stdin, setrecursionlimit
from collections import deque


def main():
    input = stdin.buffer.readline
    n = int(input())
    g = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v, w = map(int, input().split())
        g[u - 1].append([v - 1, w])
        g[v - 1].append([u - 1, w])

    ans = [-1] * n

    q = deque([0])
    ans[0] = 0

    while q:
        u = q.popleft()

        for v, w in g[u]:
            if ans[v] == -1:
                ans[v] = (ans[u] + w) % 2
                q.append(v)

    print(*ans, sep='\n')


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
