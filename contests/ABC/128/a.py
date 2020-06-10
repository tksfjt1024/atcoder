#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


def main():
    input = stdin.buffer.readline
    a, p = map(int, input().split())
    print((3 * a + p) // 2)


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
