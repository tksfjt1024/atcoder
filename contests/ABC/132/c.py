#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


def main():
    input = stdin.buffer.readline
    n = int(input())
    d = list(map(int, input().split()))
    d.sort()
    print(d[n // 2] - d[n // 2 - 1])


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
