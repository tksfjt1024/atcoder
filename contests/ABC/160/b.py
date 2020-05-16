#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


def main():
    input = stdin.buffer.readline
    x = int(input())
    ans = 0
    ans += (x // 500) * 1000
    x = x % 500
    ans += (x // 5) * 5
    print(ans)


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
