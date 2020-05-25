#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


def main():
    input = stdin.buffer.readline
    n = int(input())
    xy = [list(map(int, input().split())) for _ in range(n)]

    sum = 0

    for i in range(n - 1):
        for j in range(i + 1, n):
            xi, yi = xy[i]
            xj, yj = xy[j]
            sum += ((xi - xj) ** 2 + (yi - yj) ** 2) ** 0.5

    print(2 * sum / (n * (n - 1)) * (n - 1))


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
