#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


def main():
    input = stdin.buffer.readline
    n = int(input())
    a = list(map(int, input().split()))
    x1 = sum(a) // n
    x2 = x1 + 1
    ans1 = 0
    ans2 = 0
    for ai in a:
        ans1 += (ai - x1) ** 2
        ans2 += (ai - x2) ** 2

    print(min(ans1, ans2))


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
