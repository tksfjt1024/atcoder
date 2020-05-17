#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


def main():
    input = stdin.buffer.readline
    n, m, q = map(int, input().split())
    abcd = [list(map(int, input().split())) for _ in range(q)]

    arr = []

    def dfs(num, ai):
        if len(ai) == n:
            arr.append(ai)
        elif len(ai) < n:
            for i in range(num, m + 1):
                dfs(i, ai + [i])

    ans = 0

    dfs(1, [])

    for ai in arr:
        score = 0
        for a, b, c, d in abcd:
            if ai[b - 1] - ai[a - 1] == c:
                score += d
        if ans < score:
            ans = score

    print(ans)


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
