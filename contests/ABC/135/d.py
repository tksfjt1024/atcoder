#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


def main():
    mod = 10 ** 9 + 7
    input = stdin.buffer.readline
    s = list(input()[:-1].decode())
    n = len(s)

    dp = [0] * 13
    if s[0] == '?':
        for i in range(10):
            dp[i % 13] += 1
    else:
        dp[int(s[0]) % 13] += 1

    for i in range(1, n):
        tmp_dp = [0] * 13
        if s[i] == '?':
            for j in range(13):
                for k in range(10):
                    index = (10 * j + k) % 13
                    tmp_dp[index] += dp[j]
                    tmp_dp[index] %= mod
        else:
            for j in range(13):
                index = (10 * j + int(s[i])) % 13
                tmp_dp[index] += dp[j]
                tmp_dp[index] %= mod
        dp = tmp_dp

    print(dp[5] % mod)


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
