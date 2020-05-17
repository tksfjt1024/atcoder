#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


def gcd(x, y):
    if x % y == 0:
        return y
    return gcd(y, x % y)


def main():
    mod = 10 ** 9 + 7
    input = stdin.buffer.readline
    n = int(input())
    p = []
    m = []

    zz = 0

    for _ in range(n):
        a, b = map(int, input().split())
        if a != 0 and b != 0:
            g = gcd(a, b)
            f = b / a
            if b / a < 0:
                m.append(str(abs(a // g)) + ':' + str(abs(b // g)))
            elif f > 0:
                p.append(str(abs((b // g))) + ':' + str(abs((a // g))))
        elif a == 0 and b == 0:
            zz += 1
        elif a == 0:
            m.append(0)
        elif b == 0:
            p.append(0)

    g_p = {}
    for k in p:
        if k in g_p:
            g_p[k] += 1
        else:
            g_p[k] = 1
    g_m = {}
    for k in m:
        if k in g_m:
            g_m[k] += 1
        else:
            g_m[k] = 1

    ans = 1

    for k in g_p:
        if k in g_m:
            ans *= (2 ** g_p[k] + 2 ** g_m[k] - 1)
        else:
            ans *= 2 ** g_p[k]
        ans %= mod
    for k in g_m:
        if not (k in g_p):
            ans *= 2 ** g_m[k]
            ans %= mod
    print((ans + zz - 1) % mod)


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
