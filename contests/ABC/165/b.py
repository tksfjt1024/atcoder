#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


def main():
    input = stdin.buffer.readline
    x = int(input())
    m = 100
    ans = 0
    while m < x:
        m = int(m * 1.01)
        ans += 1
    print(ans)


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
