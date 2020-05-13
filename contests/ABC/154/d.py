#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


def main():
    input = stdin.buffer.readline
    n, k = map(int, input().split())
    p = list(map(int, input().split()))

    e = [i * (i + 1) / (2 * i) for i in range(1, 1001)]

    sum = [0] * n
    sum[0] = e[p[0] - 1]
    for i in range(1, n):
        sum[i] = sum[i - 1] + e[p[i] - 1]

    max = sum[k - 1]
    for i in range(k, n):
        if max < sum[i] - sum[i - k]:
            max = sum[i] - sum[i - k]

    print(max)


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
