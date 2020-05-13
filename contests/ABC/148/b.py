#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


def main():
    input = stdin.buffer.readline
    n = int(input())
    s, t = map(str, input().decode().split())
    s = list(s)
    t = list(t)
    ans = []
    for i in range(n):
        ans.append(s[i])
        ans.append(t[i])
    print(*ans, sep='')


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
