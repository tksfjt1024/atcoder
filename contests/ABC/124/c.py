#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


def main():
    input = stdin.buffer.readline
    s = list(input()[:-1].decode())
    n = len(s)
    l = r = -1
    ans = 0
    for i in range(1, n):
        if s[i] == s[i - 1]:
            if l == -1:
                l = i
            else:
                r = i
        if r != -1:
            ans += r - l
            r = l = -1
    if l != -1:
        ans += n - l
    print(min(ans, n - ans))


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
