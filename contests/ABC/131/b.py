#!/usr/bin/env python3

from sys import stdin, setrecursionlimit
from bisect import bisect_right


def main():
    input = stdin.buffer.readline
    n, l = map(int, input().split())
    arr = []
    for i in range(n):
        arr.append(l + i)
    arr.sort()
    print(sum(arr) - arr[min(bisect_right(arr, -1), n - 1)])


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
