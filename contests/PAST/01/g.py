#!/usr/bin/env python3

from sys import stdin, setrecursionlimit
from copy import deepcopy


def dfs(now, g, ans, n, a):
    if now == n - 1:
        tmp_ans = 0
        for gi in g:
            for i in gi:
                for j in range(n - i - 1):
                    if i + j + 1 in gi:
                        tmp_ans += a[i][j]
        if tmp_ans > ans:
            ans = tmp_ans
    else:
        for i in range(3):
            next_g = deepcopy(g)
            next_g[i].append(now + 1)
            ans = dfs(now + 1, next_g, ans, n, a)
    return ans


def main():
    input = stdin.buffer.readline
    n = int(input())
    a = [list(map(int, input().split())) for _ in range(n - 1)]
    g = [[] for _ in range(3)]
    g[0].append(0)

    ans = - (10 ** 12)

    print(dfs(0, g, ans, n, a))


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
