#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


def main():
    input = stdin.readline
    s = list(input()[:-1])
    N = len(s)
    if s != list(reversed(s)):
        print('No')
    elif s[0: (N - 1) // 2] != list(reversed(s[0: (N - 1) // 2])):
        print('No')
    elif s[(N + 1) // 2:N] != list(reversed(s[(N + 1) // 2:N])):
        print('No')
    else:
        print('Yes')


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
