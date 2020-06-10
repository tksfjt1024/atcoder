#!/usr/bin/env python3

from sys import stdin, setrecursionlimit
from bisect import bisect_left


def main():
    input = stdin.buffer.readline
    n, k = map(int, input().split())
    v = list(map(int, input().split()))

    ans = 0

    for i in range(1, k + 1):
        if i < n:
            for j in range(i + 1):
                cand = v[: j] + v[n - i + j:]
                cand.sort()
                idx = min(bisect_left(cand, 0), k - i)
                if idx > 0 or i > 0:
                    ans = max(ans, sum(cand[idx:]))

        else:
            cand = v
            cand.sort()
            idx = bisect_left(cand, 0)
            ans = max(ans, sum(cand[idx:]))

    print(ans)


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
