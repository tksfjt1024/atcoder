#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


def main():
    input = stdin.buffer.readline
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = 1
    for ai in a:
        ans *= ai
        if ans == 0:
            print(0)
            exit()
        elif ans > 10 ** 18:
            print(-1)
            exit()
    print(ans)


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
