#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


def main():
    input = stdin.buffer.readline
    n, k = map(int, input().split())
    s = list(input()[:-1].decode())
    s[k - 1] = s[k - 1].lower()
    print(*s, sep='')


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
