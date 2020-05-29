#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


def main():
    INF = float('inf')
    input = stdin.buffer.readline
    n, m = map(int, input().split())
    dp = [[INF] * (1 << n) for _ in range(m)]

    for i in range(m):
        a, b = map(int, input().split())
        c = list(map(int, input().split()))

        dp[i][0] = 0

        tmp = 0
        for ci in c:
            tmp |= 1 << (ci - 1)

        if i == 0:
            dp[i][tmp] = a
        else:
            for j in range(1 << n):
                dp[i][j] = min(dp[i][j], dp[i - 1][j])
                dp[i][j | tmp] = min(dp[i][j | tmp], dp[i - 1][j] + a)

    ans = dp[m - 1][-1]
    if ans == INF:
        print(-1)
    else:
        print(dp[m - 1][-1])


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
