#!/usr/bin/env python3

from sys import stdin, setrecursionlimit
from collections import deque


def main():
    input = stdin.buffer.readline
    n, m = map(int, input().split())
    g = [[] for _ in range(n)]
    for _ in range(m):
        u, v = map(int, input().split())
        g[u - 1].append(v - 1)
    s, t = map(int, input().split())

    q = deque()
    q.append(s - 1)
    seen = [[-1 for _ in range(3)] for _ in range(n)]
    seen[s - 1][2] = 0

    while q:
        u = q.popleft()

        for v in g[u]:
            for i in range(3):
                if seen[u][i] != -1 and seen[v][(i + 1) % 3] == -1:
                    seen[v][(i + 1) % 3] = seen[u][i] + 1
                    q.append(v)
                    if seen[t - 1][2] != -1:
                        print(seen[t - 1][2] // 3)
                        exit()
    print(-1)


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
