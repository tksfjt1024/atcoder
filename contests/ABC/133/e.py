#!/usr/bin/env python3

from sys import stdin, setrecursionlimit
from collections import deque


def main():
    input = stdin.buffer.readline
    n, k = map(int, input().split())
    g = [[] for _ in range(n)]
    for _ in range(n - 1):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        g[a].append(b)
        g[b].append(a)

    mod = 10 ** 9 + 7

    q = deque([0])
    ans = k
    seen = [False] * n
    seen[0] = True

    while q:
        v = q.popleft()
        if v == 0:
            cand = k - 1
        else:
            cand = k - 2
        for n_v in g[v]:
            if not seen[n_v]:
                seen[n_v] = True
                ans = (ans * cand) % mod
                cand -= 1
                q.append(n_v)

    print(ans)


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
