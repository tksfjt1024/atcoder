#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


def main():
    INF = float('inf')
    input = stdin.buffer.readline
    n = int(input())
    b = list(map(int, input().split()))
    b.insert(0, INF)
    b.append(INF)
    a = [0] * n

    for i in range(n):
        a[i] = min(b[i], b[i + 1])

    print(sum(a))


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
