#!/usr/bin/env python3

from sys import stdin, setrecursionlimit
from math import ceil


def main():
    input = stdin.buffer.readline
    a, b = map(int, input().split())

    set_a = set(range(ceil(a / 0.08), ceil((a + 1) / 0.08)))
    set_b = set(range(ceil(b / 0.1), ceil((b + 1) / 0.1)))

    ans = sorted(list(set_a & set_b))

    if len(ans) == 0:
        print(-1)
    else:
        print(ans[0])


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
