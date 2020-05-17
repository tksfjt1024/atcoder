#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


def main():
    input = stdin.buffer.readline
    k = int(input())
    s = input()[:-1].decode()
    if len(s) <= k:
        print(s)
    else:
        print(s[0:k], '...', sep='')


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
