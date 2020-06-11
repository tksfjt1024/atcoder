#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


def main():
    input = stdin.buffer.readline
    n = int(input())
    csf = [list(map(int, input().split())) for _ in range(n - 1)]

    for i in range(n):
        if i == n - 1:
            print(0)
        else:
            x = csf[i][1]
            for j in range(i + 1, n - 1):
                cj1, sj1, fj1 = csf[j - 1]
                cj, sj, fj = csf[j]
                # print(i, j, x, csf[j - 1], csf[j])
                if x + cj1 + (fj1 - x % fj1) % fj1 <= sj:
                    x = sj
                else:
                    x += cj1 + (fj1 - x % fj1) % fj1
            x += csf[-1][0] + (csf[-1][2] - x % csf[-1][2]) % csf[-1][2]
            print(x)


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
