#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


def main():
    input = stdin.buffer.readline
    n, k = map(int, input().split())
    h = list(map(int, input().split()))

    ans = 0
    for hi in h:
        if hi >= k:
            ans += 1

    print(ans)


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
