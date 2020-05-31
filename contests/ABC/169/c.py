#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


def main():
    input = stdin.readline
    a, b = map(str, input().split())
    a = int(a)
    b = int(b[0] + b[2:])
    print((a * b) // 100)


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
