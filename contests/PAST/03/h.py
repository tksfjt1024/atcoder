#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


def main():
    INF = 10 ** 12
    input = stdin.buffer.readline
    n, l = map(int, input().split())
    X = list(map(int, input().split()))
    x = [False] * (l + 10)
    for i in X:
        x[i] = True
    t1, t2, t3 = map(int, input().split())
    dp = [INF] * (l + 10)
    dp[0] = 0
    another = []
    another.append(INF)
    for i in range(1, l + 10):
        tmp = dp[i]
        if x[i - 1] and dp[i] > dp[i - 1] + t1 + t3:
            tmp = min(tmp, dp[i - 1] + t1 + t3)
        elif not x[i - 1] and dp[i] > dp[i - 1] + t1:
            tmp = min(tmp, dp[i - 1] + t1)

        if i >= 2:
            if x[i - 2] and dp[i] > dp[i - 2] + t1 + t2 + t3:
                tmp = min(tmp, dp[i - 2] + t1 + t2 + t3)
                if i == l + 1:
                    another.append(dp[i] - t1 // 2 - t2 // 2)
            elif not x[i - 2] and dp[i] > dp[i - 2] + t1 + t2:
                tmp = min(tmp, dp[i - 2] + t1 + t2)
                if i == l + 1:
                    another.append(dp[i] - t1 // 2 - t2 // 2)

        if i >= 4:
            if x[i - 4] and dp[i] > dp[i - 4] + t1 + 3 * t2 + t3:
                tmp = min(tmp, dp[i - 4] + t1 + 3 * t2 + t3)
                if i == l + 1:
                    another.append(dp[i] - t1 // 2 - t2 // 2)
                if i == l + 2 and i - 2 >= 0:
                    another.append(dp[i] - t1 // 2 - (3 * t2) // 2)
                if i == l + 3 and i - 3 >= 0:
                    another.append(dp[i] - t1 // 2 - (5 * t2) // 2)
            elif not x[i - 4] and dp[i] > dp[i - 4] + t1 + 3 * t2:
                tmp = min(tmp, dp[i - 4] + t1 + 3 * t2)
                if i == l + 1:
                    another.append(dp[i] - t1 // 2 - t2 // 2)
                if i == l + 2 and i - 2 >= 0:
                    another.append(dp[i] - t1 // 2 - (3 * t2) // 2)
                if i == l + 3 and i - 3 >= 0:
                    another.append(dp[i] - t1 // 2 - (5 * t2) // 2)
        dp[i] = tmp

    print(min(dp[l], *another))


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
