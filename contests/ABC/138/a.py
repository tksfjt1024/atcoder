#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


def main():
    input = stdin.buffer.readline
    a = int(input())
    s = input()[:-1].decode()

    if a >= 3200:
        print(s)
    else:
        print('red')


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
