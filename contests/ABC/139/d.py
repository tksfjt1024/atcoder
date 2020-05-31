#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


def main():
    input = stdin.buffer.readline
    n = int(input())
    print(n * (n - 1) // 2)


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
