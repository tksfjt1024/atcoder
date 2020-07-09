#!/usr/bin/env python3

from sys import stdin, setrecursionlimit
from itertools import accumulate
from bisect import bisect_left


def main():
    input = stdin.buffer.readline
    n, k = map(int, input().split())
    a = [int(input()) - k for _ in range(n)]
    summary = list(accumulate(a))
    ans = n - bisect_left(sorted(summary), 0)
    for i in range(n - 1):
        tmp = summary[i:]
        tmp.sort()
        ans += n - i - 1 - bisect_left(tmp, summary[i])

    print(ans)


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
