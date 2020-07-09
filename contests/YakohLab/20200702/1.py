#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


def main():
    input = stdin.buffer.readline
    n, h, w = map(int, input().split())
    ans = 0
    for _ in range(n):
        a, b = map(int, input().split())
        if a >= h and b >= w:
            ans += 1

    print(ans)


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
