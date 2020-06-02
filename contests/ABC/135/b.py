#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


def main():
    input = stdin.buffer.readline
    n = int(input())
    p = list(map(int, input().split()))
    count = 0
    for p, q in zip(p, sorted(p)):
        if p != q:
            count += 1

    if count > 2:
        print('NO')
    else:
        print('YES')


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
