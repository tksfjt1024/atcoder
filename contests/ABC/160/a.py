#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


def main():
    input = stdin.buffer.readline
    s = list(input()[:-1])
    if s[2] == s[3] and s[4] == s[5]:
        print('Yes')
    else:
        print('No')


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
