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
    mod = 10 ** 9 + 7
    input = stdin.buffer.readline
    x, y = map(int, input().split())

    if (x + y) % 3 != 0 or 2 * x < y or 2 * y < x:
        print(0)
    else:

        x_min = (x + y) // 3

        print(cmb((x + y) // 3, x - x_min, mod))


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
