#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


def main():
    input = stdin.buffer.readline
    a = input()[:-1].decode()
    if a == a.lower():
        print('a')
    else:
        print('A')


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
