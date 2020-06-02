#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


def main():
    input = stdin.buffer.readline
    n = int(input())
    h = list(map(int, input().split()))

    for i in range(1, n):
        if h[i] > h[i - 1]:
            h[i] -= 1
        if h[i] - h[i - 1] < 0:
            print('No')
            exit()

    print('Yes')


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
