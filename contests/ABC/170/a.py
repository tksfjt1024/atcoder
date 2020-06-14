#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


def main():
    input = stdin.buffer.readline
    x = list(map(int, input().split()))
    print(x.index(0) + 1)


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
