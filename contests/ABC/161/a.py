#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


def main():
    input = stdin.buffer.readline
    x, y, z = map(int, input().split())
    print(z, x, y)


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
