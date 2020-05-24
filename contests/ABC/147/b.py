#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


def main():
    input = stdin.buffer.readline
    s = list(input()[:-1].decode())
    n = len(s)

    ans = 0
    for i in range(n // 2):
        if s[i] != s[n - i - 1]:
            ans += 1

    print(ans)


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
