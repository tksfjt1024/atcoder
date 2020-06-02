#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


def main():
    input = stdin.buffer.readline
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    ans = 0
    tmp = 0

    for i in range(n):
        if tmp >= a[i]:
            ans += a[i]
            a[i] = 0
        else:
            ans += tmp
            a[i] -= tmp
        if b[i] >= a[i]:
            ans += a[i]
            tmp = b[i] - a[i]
        else:
            ans += b[i]
            tmp = 0

    if tmp >= a[-1]:
        ans += a[-1]
    else:
        ans += tmp

    print(ans)


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
