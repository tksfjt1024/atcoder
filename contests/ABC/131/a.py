#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


def main():
    input = stdin.buffer.readline
    s = list(input()[:-1].decode())
    if s[0] == s[1] or s[1] == s[2] or s[2] == s[3]:
        print('Bad')
    else:
        print('Good')


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
