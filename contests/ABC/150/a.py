#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


def main():
    input = stdin.buffer.readline
    k, x = map(int, input().split())
    print('Yes') if 500 * k >= x else print('No')


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
