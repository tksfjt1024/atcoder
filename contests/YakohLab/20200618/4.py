#!/usr/bin/env python3

from sys import stdin, setrecursionlimit
from collections import defaultdict


def main():
    input = stdin.buffer.readline
    n, d, a = map(int, input().split())
    x_arr = []
    h_arr = []
    for _ in range(n):
        xi, hi = map(int, input().split())
        x_arr.append(xi)
        h_arr.append(hi)
    x_max = max(x_arr)

    dp = {}
    for x, h in zip(x_arr, h_arr):
        dp[x] = h

    ans = 0
    summary = [0] * (x_max + 2 + 2 * d)
    for i in range(1, x_max + 1):
        if i in dp:
            summary[i] += dp[i]
            summary[i + 1] -= dp[i]
        summary[i] += summary[i - 1]
        if i in dp and dp[i] > 0:
            count = 0
            if summary[i] % a == 0:
                count = summary[i] // a
            else:
                count = (summary[i] + 1) // a
            ans += count
            summary[i] -= count * a
            summary[i + 2 * d + 1] += count * a

    print(ans)


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
