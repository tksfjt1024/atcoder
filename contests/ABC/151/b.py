#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


def main():
    n, k, m = map(int, stdin.readline().split())
    a = list(map(int, stdin.readline().split()))
    aim = n * m - sum(a)
    if 0 <= aim <= k:
        print(aim)
    elif aim < 0:
        print(0)
    else:
        print(-1)


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
