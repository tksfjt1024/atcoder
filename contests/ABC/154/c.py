#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


def main():
    input = stdin.buffer.readline
    n = int(input())
    a = len(set(list(map(int, input().split()))))
    print('YES') if n == a else print('NO')


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
