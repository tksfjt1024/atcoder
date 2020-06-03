#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


def main():
    input = stdin.buffer.readline
    n = int(input())
    a = list(map(int, input().split()))
    x_sum = sum(a) // 2
    x = [0] * n
    tmp = x_sum
    idx = 1
    for _ in range((n - 1) // 2):
        tmp -= a[idx]
        idx += 2
        idx %= n
    x[0] = 2 * tmp
    for i in range(n - 1):
        x[i + 1] = 2 * (a[i] - x[i] // 2)
    print(*x)


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
