#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


def main():
    input = stdin.buffer.readline
    n = int(input())
    h = list(map(int, input().split()))

    max = 0
    count = 0

    for i in range(1, n):
        if h[i] <= h[i - 1]:
            count += 1
        else:
            if count > max:
                max = count
            count = 0

    if count > max:
        max = count

    print(max)


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
