#!/usr/bin/env python3

from sys import stdin, setrecursionlimit
from collections import defaultdict


def main():
    input = stdin.buffer.readline
    n = int(input())
    a = list(map(int, input().split()))

    ans = 0

    dic = defaultdict(int)
    for ai in a:
        dic[ai - 1] += 1
        dic[ai] += 1
        dic[ai + 1] += 1
        ans = max(ans, dic[ai - 1], dic[ai], dic[ai + 1])

    print(ans)


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
