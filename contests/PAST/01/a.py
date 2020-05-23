#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


def main():
    input = stdin.buffer.readline
    try:
        s = int(input())
        print(2 * s)
    except:
        print('error')


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
