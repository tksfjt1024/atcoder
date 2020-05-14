#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


def cmb(n, r, mod=10 ** 9 + 7):
    r = min(r, n - r)
    x = y = 1
    for i in range(r):
        x *= n - i
        x %= mod
        y *= i + 1
        y %= mod
    return x * pow(y, mod - 2, mod) % mod


def main():
    input = stdin.buffer.readline
    n, a, b = map(int, input().split())
    mod = 10 ** 9 + 7

    print((pow(2, n, mod) - 1 - cmb(n, a, mod) - cmb(n, b, mod)) % mod)


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
