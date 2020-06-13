#!/usr/bin/env python3

from sys import stdin, setrecursionlimit
from itertools import accumulate


def main():
    input = stdin.buffer.readline
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    for i in range(k):
        tmp = [0] * (n + 1)
        for j in range(n):
            tmp[max(0, j - a[j])] += 1
            tmp[min(n, j + a[j] + 1)] -= 1
        a = list(accumulate(tmp))[:n]
        for ai in a:
            if ai != n:
                break
        else:
            break
    print(*a)


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
