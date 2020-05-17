#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


def main():
    input = stdin.buffer.readline
    n = int(input())
    ans = 0
    for i in range(1, n + 1):
        if i % 3 != 0 and i % 5 != 0:
            ans += i
    print(ans)


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
