#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


def main():
    input = stdin.buffer.readline
    N, M, Q = map(int, input().split())
    points = [N] * Q
    seen = [[] for _ in range(N)]
    s = [list(map(int, input().split())) for _ in range(Q)]
    for i in range(Q):
        if s[i][0] == 1:
            n = s[i][1] - 1
            score = 0
            for mi in range(M):
                if mi in seen[n]:
                    score += points[mi]
            print(score)
        elif s[i][0] == 2:
            n, m = s[i][1] - 1, s[i][2] - 1
            points[m] -= 1
            seen[n].append(m)


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
