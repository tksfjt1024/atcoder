#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


def gcd(x, y):
    if x % y == 0:
        return y
    return gcd(y, x % y)


def main():
    input = stdin.buffer.readline
    k = int(input())
    g = []
    for i in range(1, k + 1):
        gi = []
        for j in range(1, k + 1):
            gi.append(gcd(i, j))
        g.append(gi)
    ans = 0
    for a in range(k):
        for b in range(k):
            for c in range(k):
                tmp = g[a][b] - 1
                ans += g[tmp][c]
    print(ans)


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
