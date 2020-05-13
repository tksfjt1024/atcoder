#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


def main():
    input = stdin.buffer.readline
    s, t = map(str, input().decode().split())
    print(t, s, sep='')


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
