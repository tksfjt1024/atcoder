#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


def main():
    input = stdin.readline
    s, t = map(str, input().split())
    a, b = map(int, input().split())
    u = input()[:-1]
    print(a - 1, b) if s == u else print(a, b - 1)


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
