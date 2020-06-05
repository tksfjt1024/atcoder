#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


def main():
    input = stdin.buffer.readline
    n = int(input())
    ab = [list(map(int, input().split())) for _ in range(n)]
    ab.sort(key=lambda x: (x[1], -x[0]))
    d = 0
    for a, b in ab:
        d += a
        if d > b:
            print('No')
            exit()
    print('Yes')


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
