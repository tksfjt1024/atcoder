#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


def main():
    input = stdin.buffer.readline
    a, b = map(int, input().split())
    arr = [a, b, a - 1, b - 1]
    arr.sort()
    print(arr[2] + arr[3])


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
