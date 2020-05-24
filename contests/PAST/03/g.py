#!/usr/bin/env python3

from sys import stdin, setrecursionlimit
from collections import deque


def main():
    input = stdin.buffer.readline
    n, x, y = map(int, input().split())
    g = [[[] for _ in range(403)] for _ in range(403)]
    for _ in range(n):
        xi, yi = map(int, input().split())
        xi += 201
        yi += 201
        if xi - 1 >= 0:
            g[xi - 1][yi].append([xi, yi])
            if yi - 1 >= 0:
                g[xi - 1][yi - 1].append([xi, yi])
        if xi + 1 <= 402:
            g[xi + 1][yi].append([xi, yi])
            if yi - 1 >= 0:
                g[xi + 1][yi - 1].append([xi, yi])
        if yi - 1 >= 0:
            g[xi][yi - 1].append([xi, yi])
        if yi + 1 <= 402:
            g[xi][yi + 1].append([xi, yi])

    d = [[10 ** 12 for _ in range(403)] for _ in range(403)]

    q = deque()

    d[201][201] = 0
    q.append([201, 201])

    while q:
        xi, yi = q.popleft()
        gi = g[xi][yi]

        if xi + 1 <= 402 and not [xi + 1, yi] in gi and d[xi + 1][yi] > d[xi][yi] + 1:
            d[xi + 1][yi] = d[xi][yi] + 1
            q.append([xi + 1, yi])

        if yi + 1 <= 402 and not [xi, yi + 1] in gi and d[xi][yi + 1] > d[xi][yi] + 1:
            d[xi][yi + 1] = d[xi][yi] + 1
            q.append([xi, yi + 1])

        if xi - 1 >= 0 and not [xi - 1, yi] in gi and d[xi - 1][yi] > d[xi][yi] + 1:
            d[xi - 1][yi] = d[xi][yi] + 1
            q.append([xi - 1, yi])

        if yi - 1 >= 0 and not [xi, yi - 1] in gi and d[xi][yi - 1] > d[xi][yi] + 1:
            d[xi][yi - 1] = d[xi][yi] + 1
            q.append([xi, yi - 1])

        if xi + 1 <= 402 and yi + 1 <= 402 and not [xi + 1, yi + 1] in gi and d[xi + 1][yi + 1] > d[xi][yi] + 1:
            d[xi + 1][yi + 1] = d[xi][yi] + 1
            q.append([xi + 1, yi + 1])

        if xi - 1 >= 0 and yi + 1 <= 402 and not [xi - 1, yi + 1] in gi and d[xi - 1][yi + 1] > d[xi][yi] + 1:
            d[xi - 1][yi + 1] = d[xi][yi] + 1
            q.append([xi - 1, yi + 1])

    ans = d[x + 201][y + 201]
    if ans == 10 ** 12:
        print(-1)
    else:
        print(ans)


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
