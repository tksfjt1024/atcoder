#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


def main():
    input = stdin.buffer.readline
    r = int(input())
    print(2 * r * 3.14)


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
