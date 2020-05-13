#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


def main():
    input = stdin.buffer.readline
    s = list(input()[:-1])
    print('x' * len(s))


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
