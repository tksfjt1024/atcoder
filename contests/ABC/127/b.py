#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


def main():
    input = stdin.buffer.readline
    r, d, x = map(int, input().split())
    for _ in range(10):
        x = r * x - d
        print(x)


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
