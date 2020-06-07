#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


def main():
    input = stdin.buffer.readline
    n, x = map(int, input().split())
    l = list(map(int, input().split()))

    ans = 1
    d = 0
    for li in l:
        if d + li <= x:
            ans += 1
            d += li
        else:
            break
    print(ans)


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
