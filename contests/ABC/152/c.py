#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


def main():
    input = stdin.buffer.readline
    n = int(input())
    p = list(map(int, input().split()))
    min = p[0]
    ans = 1
    for i in range(1, n):
        if p[i] <= min:
            min = p[i]
            ans += 1
    print(ans)


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
