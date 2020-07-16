#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


def main():
    input = stdin.buffer.readline
    h, w, k = map(int, input().split())
    m = [list(input()[:-1].decode()) for _ in range(h)]
    ans = [[0] * w for _ in range(h)]
    num = 1
    for i in range(h):
        indexes = [j for j in range(w) if m[i][j] == '#']
        n = len(indexes)
        if n == 0:
            if ans[i - 1].count(0) == 0:
                ans[i] = ans[i - 1]
        else:
            for j in range(w):
                ans[i][j] = num
                if (j in indexes and indexes[-1] != j) or j == w - 1:
                    num += 1

    for i in reversed(range(h - 1)):
        if ans[i].count(0) == w:
            ans[i] = ans[i + 1]

    for i in range(h):
        if ans[i].count(0) == w:
            ans[i] = [1] * w

    for a in ans:
        print(*a)


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
