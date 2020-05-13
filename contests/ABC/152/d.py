#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


def main():
    input = stdin.buffer.readline
    n = int(input())
    default = 0

    c = [[0] * 10 for _ in range(10)]

    for i in range(1, n + 1):
        i = str(i)
        c[int(i[0])][int(i[-1])] += 1

    ans = 0
    for i in range(10):
        for j in range(10):
            ans += c[i][j] * c[j][i]

    print(ans)


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
