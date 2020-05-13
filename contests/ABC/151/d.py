#!/usr/bin/env python3

from collections import deque

from sys import stdin, setrecursionlimit


def main():
    h, w = map(int, stdin.readline().split())
    g = [list(map(str, list(input()))) for _ in range(h)]

    ans = 0

    for i in range(h):
        for j in range(w):
            if g[i][j] == '.':
                d = [[-1 for _ in range(w)] for _ in range(h)]
                q = deque()

                d[i][j] = 0
                q.append([i, j])

                while q:
                    vi, vj = q.popleft()

                    if vi > 0:
                        if g[vi - 1][vj] == '.' and d[vi - 1][vj] == -1:
                            d[vi - 1][vj] = d[vi][vj] + 1
                            q.append([vi - 1, vj])
                    if vi < h - 1:
                        if g[vi + 1][vj] == '.' and d[vi + 1][vj] == -1:
                            d[vi + 1][vj] = d[vi][vj] + 1
                            q.append([vi + 1, vj])
                    if vj > 0:
                        if g[vi][vj - 1] == '.' and d[vi][vj - 1] == -1:
                            d[vi][vj - 1] = d[vi][vj] + 1
                            q.append([vi, vj - 1])
                    if vj < w - 1:
                        if g[vi][vj + 1] == '.' and d[vi][vj + 1] == -1:
                            d[vi][vj + 1] = d[vi][vj] + 1
                            q.append([vi, vj + 1])
                tmp_max = 0
                for hi in range(h):
                    for wj in range(w):
                        tmp_max = max(tmp_max, d[hi][wj])
                ans = max(ans, tmp_max)

    print(ans)


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
