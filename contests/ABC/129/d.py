#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


def main():
    input = stdin.buffer.readline
    h, w = map(int, input().split())
    col = [[0, w + 1] for _ in range(h)]
    row = [[0, h + 1] for _ in range(w)]
    for i in range(h):
        s = list(input()[:-1].decode())
        for j in range(w):
            if s[j] == '#':
                col[i].append(j + 1)
                row[j].append(i + 1)

    cc = [[0] * (w + 2) for _ in range(h)]
    rc = [[0] * (h + 2) for _ in range(w)]

    for i in range(h):
        col[i].sort()
        for j in range(len(col[i]) - 1):
            cc[i][col[i][j] + 1:col[i][j + 1]] = [col[i][j + 1] - col[i][j] - 1] * (col[i][j + 1] - col[i][j] - 1)

    for i in range(w):
        row[i].sort()
        for j in range(len(row[i]) - 1):
            rc[i][row[i][j] + 1:row[i][j + 1]] = [row[i][j + 1] - row[i][j] - 1] * (row[i][j + 1] - row[i][j] - 1)

    ans = 0
    for i in range(h):
        for j in range(w):
            ans = max(ans, cc[i][j + 1] + rc[j][i + 1] - 1)

    print(ans)


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
