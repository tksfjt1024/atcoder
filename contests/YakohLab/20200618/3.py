#!/usr/bin/env python3

from sys import stdin, setrecursionlimit
from itertools import accumulate


def main():
    input = stdin.buffer.readline
    MAX = 10 ** 5
    q = int(input())
    lr = [list(map(int, input().split())) for _ in range(q)]

    dp = [1] * (MAX + 1)
    dp[0] = dp[1] = 0
    for i in range(2, MAX + 1):
        if dp[i]:
            x = 2
            while i * x < MAX + 1:
                dp[i * x] = 0
                x += 1
    for i in reversed(range(2, MAX + 1)):
        if not dp[(i + 1) // 2]:
            dp[i] = 0

    summary = list(accumulate(dp))

    for l, r in lr:
        print(summary[r] - summary[l - 1])


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
