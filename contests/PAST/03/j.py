#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


def main():
    input = stdin.buffer.readline
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    max = [0] * n
    for ai in a:
        ans = -1
        for i in range(n):
            if max[i] < ai:
                max[i] = ai
                ans = i + 1
                break
        print(ans)


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
