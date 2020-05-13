#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


def main():
    h, n = map(int, stdin.readline().split())
    ab = []
    max_a = 0
    for _ in range(n):
        a, b = map(int, stdin.readline().split())
        if a > max_a:
            max_a = a
        ab.append([a / b, a, b])

    ab.sort(reverse=True)

    dp = [0] * (h + max_a)

    for i in range(h + max_a):
        dp[i] = (i // ab[0][1] + 1) * ab[0][2]

    for i in range(h):
        for j in range(n):
            dp[i + ab[j][1]] = min(dp[i + ab[j][1]], dp[i] + ab[j][2])

    print(min(dp[h - 1:]))


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
