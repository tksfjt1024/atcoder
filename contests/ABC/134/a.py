#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


def main():
    input = stdin.buffer.readline
    r = int(input())
    print(3 * r ** 2)


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
