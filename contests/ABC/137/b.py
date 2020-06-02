#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


def main():
    input = stdin.buffer.readline
    k, x = map(int, input().split())
    print(*list(range(x - k + 1, x + k)))


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
