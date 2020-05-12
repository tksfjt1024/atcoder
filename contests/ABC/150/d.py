#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


def gcd(x, y):
    if x % y == 0:
        return y
    return gcd(y, x % y)


def main():
    input = stdin.buffer.readline
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a = [a[i] // 2 for i in range(n)]
    a = list(set(a))
    n = len(a)
    lcm = 1
    for i in range(n):
        lcm = lcm * a[i] // gcd(lcm, a[i])
    for i in range(n):
        if (lcm // a[i] % 2) == 0:
            print(0)
            exit()
    ans = m // lcm
    print(ans - ans // 2)


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
