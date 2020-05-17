#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


def main():
    input = stdin.buffer.readline
    n = int(input())
    a = list(map(int, input().split()))

    g = [0] * n
    for ai in a:
        g[ai - 1] += 1
    print(*g, sep='\n')


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
