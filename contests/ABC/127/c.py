#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


def main():
    input = stdin.buffer.readline
    n, m = map(int, input().split())
    l_max = 0
    r_min = float('inf')
    for _ in range(m):
        l, r = map(int, input().split())
        l_max = max(l_max, l)
        r_min = min(r_min, r)
    print(max(r_min + 1 - l_max, 0))


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
