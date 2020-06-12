#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


def main():
    input = stdin.buffer.readline
    s = input()[:-1].decode()
    l = int(s[:2])
    r = int(s[2:])
    if (l >= 13 or l == 0) and 1 <= r <= 12:
        print('YYMM')
    elif 1 <= l <= 12 and (r >= 13 or r == 0):
        print('MMYY')
    elif 1 <= l <= 12 and 1 <= r <= 12:
        print('AMBIGUOUS')
    else:
        print('NA')


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
