#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


def main():
    mod = 10 ** 9 + 7
    input = stdin.buffer.readline
    n, m = map(int, input().split())
    a = [1] * (n + 1)
    for _ in range(m):
        idx = int(input())
        a[idx] = 0

    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = a[i - 1] * dp[i - 1] + a[i - 2] * dp[i - 2]
        dp[i] %= mod

    print(dp[-1] % mod)


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
