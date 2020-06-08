#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


def main():
    input = stdin.buffer.readline
    n = int(input())
    w = list(map(int, input().split()))
    s1 = 0
    s2 = sum(w)
    ans = float('inf')

    for wi in w:
        s1 += wi
        s2 -= wi
        ans = min(ans, abs(s2 - s1))

    print(ans)


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
