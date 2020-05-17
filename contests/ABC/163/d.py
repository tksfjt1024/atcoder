#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


def main():
    mod = 10 ** 9 + 7
    input = stdin.buffer.readline
    n, k = map(int, input().split())
    ans = 0
    for i in range(k, n + 2):
        ans += (n - i + 1) * i + 1
    print(ans % mod)


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
