#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


def main():
    input = stdin.buffer.readline
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    max_a = max(a)

    dp = [True] * (max_a + 1)
    ans = 0

    for i in range(n):
        ai = a[i]
        if dp[ai]:
            if not (i < n - 1 and a[i] == a[i + 1]):
                ans += 1
            x = 1
            while ai * x < max_a + 1:
                dp[ai * x] = False
                x += 1

    print(ans)


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
