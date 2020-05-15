#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


def main():
    input = stdin.buffer.readline
    n, a, b = map(int, input().split())

    mod = n % (a + b)

    print(n // (a + b) * a + min(mod, a))


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
