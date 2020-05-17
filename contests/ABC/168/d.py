#!/usr/bin/env python3

from sys import stdin, setrecursionlimit
from collections import deque


def main():
    input = stdin.buffer.readline
    n, m = map(int, input().split())
    g = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        g[a - 1].append(b - 1)
        g[b - 1].append(a - 1)

    result = []

    d = [[10 ** 12, -1] for _ in range(n)]
    d[0] = [0, 0]

    q = deque()
    q.append(0)

    while q:
        now_i = q.popleft()

        for next_i in g[now_i]:
            if d[next_i][0] > d[now_i][0] + 1:
                d[next_i] = [d[now_i][0] + 1, now_i]
                q.append(next_i)

    for di in d:
        if di[0] == 10 ** 12:
            print('No')
            exit()

    print('Yes')
    for di in d[1:]:
        print(di[1] + 1)


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
