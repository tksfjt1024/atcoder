#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


def main():
    MOD = 998244353
    input = stdin.buffer.readline
    n, s = map(int, input().split())
    a = list(map(int, input().split()))
    dp = [0] * (s + 1)
    dp[0] = 1

    for i in range(n):
        tmp = [0] * (s + 1)
        for j in range(s + 1):
            tmp[j] += 2 * dp[j]
            tmp[j] %= MOD
            if j + a[i] <= s:
                tmp[j + a[i]] += dp[j]
                tmp[j + a[i]] %= MOD

        dp = tmp

    print(dp[-1] % MOD)


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
