#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


def main():
    input = stdin.buffer.readline
    a, v = map(int, input().split())
    b, w = map(int, input().split())
    t = int(input())
    if (v - w) * t >= abs(b - a):
        print('YES')
    else:
        print('NO')


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
