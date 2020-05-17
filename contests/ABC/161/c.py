#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


def main():
    input = stdin.buffer.readline
    n, k = map(int, input().split())
    mod = n % k
    print(min(mod, k - mod))


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
