#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


def main():
    input = stdin.buffer.readline
    a, b, c = map(int, input().split())
    print(max([c - a + b, 0]))


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
