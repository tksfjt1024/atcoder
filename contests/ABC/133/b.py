#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


def main():
    input = stdin.buffer.readline
    n, d = map(int, input().split())
    x = [list(map(int, input().split())) for _ in range(n)]
    ans = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            dd = sum([(x[i][k] - x[j][k]) ** 2 for k in range(d)])
            if dd == int(dd ** 0.5) ** 2:
                ans += 1
    print(ans)


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
