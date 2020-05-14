#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


def main():
    input = stdin.buffer.readline
    n, k = map(int, input().split())
    ans = []
    while n > 0:
        ans.insert(0, n % k)
        n = n // k
    print(len(ans))


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
