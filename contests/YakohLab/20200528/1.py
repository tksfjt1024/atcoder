#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


def main():
    input = stdin.buffer.readline
    n = int(input())
    a = [list(map(int, input().split())) for _ in range(2)]

    max = 0

    for i in range(n):
        tmp = 0
        for j in range(i + 1):
            tmp += a[0][j]
        for j in range(i, n):
            tmp += a[1][j]

        if tmp > max:
            max = tmp

    print(max)


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
