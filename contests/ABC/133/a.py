#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


def main():
    input = stdin.buffer.readline
    n, a, b = map(int, input().split())
    print(min(n * a, b))


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
