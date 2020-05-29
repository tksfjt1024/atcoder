#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


def main():
    input = stdin.buffer.readline
    n = int(input())
    a = list(map(int, input().split()))

    summary = []

    for i in range(n):
        summary.append([a[i], i])

    summary.sort()

    print(*[summary[i][1] + 1 for i in range(n)])


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
