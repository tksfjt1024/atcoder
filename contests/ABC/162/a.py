#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


def main():
    input = stdin.buffer.readline
    n = list(input()[:-1].decode())
    print('Yes') if n.count('7') > 0 else print('No')


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
