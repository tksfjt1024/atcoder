#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


def main():
    input = stdin.buffer.readline
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        if a[a[i] - 1] == i + 1:
            ans += 1
    print(ans // 2)


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
