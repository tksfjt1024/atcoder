#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


def main():
    input = stdin.buffer.readline
    n = int(input())
    a = list(map(int, input().split()))
    ave = sum(a) / n
    ans = 0
    for i in range(n):
        ai = a[i]
        if abs(ai - ave) < abs(a[ans] - ave):
            ans = i
    print(ans)


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
