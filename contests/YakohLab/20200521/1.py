#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


def main():
    input = stdin.buffer.readline
    x, y = map(int, input().split())
    count = 0
    tmp = x
    while tmp <= y:
        tmp *= 2
        count += 1
    print(count)


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
