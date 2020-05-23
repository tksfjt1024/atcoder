#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


def main():
    input = stdin.buffer.readline
    arr = list(map(int, input().split()))
    arr.sort()
    print(arr[-3])


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
