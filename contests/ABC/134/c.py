#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


def main():
    input = stdin.buffer.readline
    n = int(input())
    d = [int(input()) for _ in range(n)]
    s_d = sorted(d)
    max = s_d[-1]
    for di in d:
        if di == s_d[-1]:
            print(s_d[-2])
        else:
            print(max)


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
