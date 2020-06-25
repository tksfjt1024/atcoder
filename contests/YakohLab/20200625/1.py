#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


def main():
    input = stdin.readline
    n = int(input())
    a = list(input()[:-1])
    b = list(input()[:-1])
    c = list(input()[:-1])

    ans = 0
    for ai, bi, ci in zip(a, b, c):
        ans += len(list(set([ai, bi, ci]))) - 1

    print(ans)


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
