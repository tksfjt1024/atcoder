#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


def main():
    input = stdin.buffer.readline
    n, m = map(int, input().split())
    sum_a = sum(list(map(int, input().split())))
    ans = n - sum_a
    if ans < 0:
        print(-1)
    else:
        print(ans)


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
