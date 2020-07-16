#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


def main():
    input = stdin.buffer.readline
    s = list(input()[:-1].decode())
    a_count = s.count('a')
    b_count = s.count('b')
    c_count = s.count('c')
    arr = sorted([a_count, b_count, c_count])
    if max(arr) - min(arr) > 1:
        print('NO')
    else:
        print('YES')


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
