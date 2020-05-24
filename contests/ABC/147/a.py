#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


def main():
    input = stdin.buffer.readline
    a = map(int, input().split())
    if sum(a) >= 22:
        print('bust')
    else:
        print('win')


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
