#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


def main():
    h, a = map(int, stdin.readline().split())
    ans = 0
    while h > 0:
        h -= a
        ans += 1
    print(ans)


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
