#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


def main():
    input = stdin.buffer.readline
    n, m, q = map(int, input().split())
    g = [[] for _ in range(n)]
    for _ in range(m):
        u, v = map(int, input().split())
        g[u - 1].append(v - 1)
        g[v - 1].append(u - 1)
    c = list(map(int, input().split()))
    s = [list(map(int, input().split())) for _ in range(q)]

    for si in s:
        if si[0] == 1:
            x = si[1] - 1
            print(c[x])
            for n_v in g[x]:
                c[n_v] = c[x]
        elif si[0] == 2:
            x, y = si[1] - 1, si[2]
            print(c[x])
            c[x] = y


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
