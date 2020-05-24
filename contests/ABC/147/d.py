#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


def main():
    mod = 10 ** 9 + 7
    input = stdin.buffer.readline
    n = int(input())
    a = list(map(int, input().split()))

    counts = [0] * 60

    for ai in a:
        for i in range(60):
            if ai & (1 << i):
                counts[i] += 1

    ans = 0
    base = 0

    for c in counts:
        ans += c * (n - c) * (1 << base)
        ans %= mod
        base += 1

    print(ans % mod)


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
