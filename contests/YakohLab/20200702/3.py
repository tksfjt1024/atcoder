#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


def main():
    input = stdin.buffer.readline
    n = int(input())
    xl = [list(map(int, input().split())) for _ in range(n)]
    xl.sort()
    ans1 = 0
    max1 = -float('inf')
    ans2 = 0
    max2 = -float('inf')
    for i in range(n):
        x, l = xl[i]
        if i == 0:
            if max1 <= x - l:
                ans1 += 1
                max1 = x + l
        else:
            if max1 <= x - l:
                ans1 += 1
                max1 = x + l
            if max2 <= x - l:
                ans2 += 1
                max2 = x + l
    print(max(ans1, ans2))


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
