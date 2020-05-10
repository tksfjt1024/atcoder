#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


def main():
    input = stdin.buffer.readline
    s = list(input()[:-1])
    t = list(input()[:-1])
    s_len = len(s)
    t_len = len(t)
    print('Yes') if s_len + 1 == t_len and s == t[0:s_len] else print('No')


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
