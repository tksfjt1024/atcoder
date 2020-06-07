#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


def main():
    input = stdin.buffer.readline
    x, a = map(int, input().split())
    if x < a:
        print(0)
    else:
        print(10)


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
