#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


def main():
    input = stdin.buffer.readline
    s = list(input()[:-1].decode())
    s.sort()
    if s[0] == s[1] and s[1] != s[2] and s[2] == s[3]:
        print('Yes')
    else:
        print('No')


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
