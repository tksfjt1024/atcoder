#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


def main():
    input = stdin.buffer.readline
    a, r, n = map(int, input().split())
    for _ in range(n - 1):
        a *= r
        if a > 10 ** 9:
            print('large')
            exit()
    print(a)


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
