#!/usr/bin/env python3

from sys import stdin, setrecursionlimit
from collections import defaultdict


def main():
    input = stdin.readline
    n = int(input())
    dic = defaultdict(list)
    for i in range(1, n + 1):
        s, p = map(str, input().split())
        dic[s].append([int(p), i])
        dic[s].sort(reverse=True)
    s_dic = sorted(dic.items(), key=lambda x: x[0])

    for k, arr in s_dic:
        for ai in arr:
            print(ai[1])


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
