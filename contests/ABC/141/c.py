#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


def main():
    input = stdin.buffer.readline
    n, k, q = map(int, input().split())
    scores = [0] * n
    for _ in range(q):
        a = int(input())
        scores[a - 1] += 1
    for i in range(n):
        scores[i] = k - q + scores[i]

    for si in scores:
        if si <= 0:
            print('No')
        else:
            print('Yes')


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
