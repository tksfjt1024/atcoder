#!/usr/bin/env python3

from sys import stdin, setrecursionlimit
from collections import defaultdict


def main():
    input = stdin.buffer.readline
    n = int(input())
    a = list(map(int, input().split()))
    dic = defaultdict(int)
    max_1 = 0
    max_2 = 0
    for ai in a:
        dic[ai] += 1
        if dic[ai] >= 2 and ai > max_1:
            max_2 = max_1
            max_1 = ai
        if dic[ai] >= 2 and max_1 > ai > max_2:
            max_2 = ai
    if dic[max_1] >= 4:
        print(max_1 ** 2)
    else:
        print(max_1 * max_2)


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
