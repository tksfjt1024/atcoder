#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


def main():
    input = stdin.buffer.readline
    ab = [list(map(int, input().split())) for _ in range(3)]
    count = [0] * 4
    for a, b in ab:
        count[a - 1] += 1
        count[b - 1] += 1
    if count.count(3) >= 1:
        print('NO')
    else:
        print("YES")


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
