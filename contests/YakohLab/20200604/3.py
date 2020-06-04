#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


def main():
    input = stdin.buffer.readline
    n = int(input())
    s = input()[:-1].decode()
    c1 = 0
    c2 = 0
    for i in range(n):
        if s[i] == '(':
            c1 += 1
        elif s[i] == ')':
            c1 -= 1
        if c1 < 0:
            c1 = 0
            c2 += 1
    print('(' * c2, s, ')' * c1, sep='')


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
