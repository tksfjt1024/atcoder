#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


def main():
    input = stdin.buffer.readline
    n = int(input())
    a = list(map(int, input().split()))

    num = 1
    for ai in a:
        num *= ai

    den = sum([num // a[i] for i in range(n)])

    print(num / den)


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
