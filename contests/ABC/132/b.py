#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


def main():
    input = stdin.buffer.readline
    n = int(input())
    p = list(map(int, input().split()))
    ans = 0
    for i in range(n - 2):
        tmp = p[i: i + 3]
        tmp.sort()
        if tmp[1] == p[i + 1]:
            ans += 1

    print(ans)


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
