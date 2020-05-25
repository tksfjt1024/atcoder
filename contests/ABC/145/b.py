#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


def main():
    input = stdin.buffer.readline
    n = int(input())
    s = input()[:-1]
    if n % 2 == 0 and s[0: n // 2] == s[n // 2:n]:
        print('Yes')
    else:
        print('No')


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
