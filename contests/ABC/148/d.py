#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


def gcd(x, y):
    if x % y == 0:
        return y
    return gcd(y, x % y)


def main():
    input = stdin.buffer.readline
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    num = 1
    for ai in a:
        if ai == num:
            num += 1
        else:
            ans += 1
    if num == 1:
        print(-1)
    else:
        print(ans)


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
