#!/usr/bin/env python3

from sys import stdin, setrecursionlimit
from collections import defaultdict


def main():
    input = stdin.buffer.readline
    n = int(input())
    a = list(map(int, input().split()))
    ans = sum(a)
    dic = defaultdict(int)
    for ai in a:
        dic[ai] += 1
    q = int(input())
    bc = [list(map(int, input().split())) for _ in range(q)]
    for b, c in bc:
        count = dic[b]
        ans += count * (c - b)
        print(ans)
        dic[b] -= count
        dic[c] += count


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
