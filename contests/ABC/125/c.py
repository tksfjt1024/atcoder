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

    l = [0] * (n - 1)
    r = [0] * (n - 1)
    l[0] = a[0]
    r[-1] = a[-1]

    for i in range(1, n - 1):
        l[i] = gcd(l[i - 1], a[i])
        r[n - 2 - i] = gcd(r[n - 1 - i], a[n - 1 - i])

    ans = 0
    for i in range(n):
        if i == 0:
            ans = max(ans, r[i])
        elif i == n - 1:
            ans = max(ans, l[i - 1])
        else:
            ans = max(ans, gcd(l[i - 1], r[i]))

    print(ans)


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
