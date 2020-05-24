#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


def main():
    input = stdin.buffer.readline
    s = input()[:-1].decode()
    t = input()[:-1].decode()

    if s == t:
        print('same')
    elif s.lower() == t.lower():
        print('case-insensitive')
    else:
        print('different')


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
