#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


def main():
    input = stdin.buffer.readline
    x, n = map(int, input().split())
    p = list(map(int, input().split()))
    arr = []
    for i in range(-100, 201):
        if not i in p:
            arr.append(i)
    ans = arr[0]
    for ai in arr:
        if abs(ai - x) < abs(ans - x):
            ans = ai
    print(ans)


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
