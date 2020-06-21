#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


def main():
    input = stdin.buffer.readline
    n = int(input())
    a = list(map(int, input().split()))
    ans = []
    s = 0
    for ai in a:
        s = s ^ ai
    for i in range(n):
        ans.append(s ^ (a[i]))
    print(*ans)


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
