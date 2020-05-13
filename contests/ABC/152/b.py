#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


def main():
    input = stdin.buffer.readline
    a, b = map(int, input().split())
    print(str(a) * b) if a < b else print(str(b) * a)


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
