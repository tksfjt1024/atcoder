#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


def main():
    mod = 10 ** 9 + 7
    input = stdin.buffer.readline
    n = int(input())
    s1 = list(input()[:-1].decode())
    s2 = list(input()[:-1].decode())
    ans = 0
    if s1[0] == s2[0]:
        ans = 3
    else:
        ans = 6
    for i in range(1, n):
        if s1[i - 1] == s2[i - 1]:
            if s1[i] == s2[i]:
                ans *= 2
            else:
                ans *= 2
            ans %= mod
        else:
            if s1[i - 1] == s1[i] and s2[i - 1] == s2[i]:
                ans *= 1
            elif s1[i] != s2[i]:
                ans *= 3
            else:
                ans *= 1
            ans %= mod
    print(ans % mod)


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
