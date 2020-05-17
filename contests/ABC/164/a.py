#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


def main():
    input = stdin.buffer.readline
    s, w = map(int, input().split())
    if s <= w:
        print('unsafe')
    else:
        print('safe')


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
