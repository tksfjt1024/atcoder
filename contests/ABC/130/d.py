#!/usr/bin/env python3

from sys import stdin, setrecursionlimit
from bisect import bisect_left


def main():
    input = stdin.buffer.readline
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    summary = [0]
    tmp = 0
    for ai in a:
        tmp += ai
        summary.append(tmp)

    ans = 0
    for num in summary:
        ans += n + 1 - bisect_left(summary, num + k)
    print(ans)


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
