#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


def main():
    input = stdin.buffer.readline
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    limit = sum(a) / (4 * m)
    count = 0
    for i in range(n):
        if a[i] >= limit:
            count += 1
    if count >= m:
        print('Yes')
    else:
        print('No')


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
