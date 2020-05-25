#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


def main():
    input = stdin.buffer.readline
    n = int(input())
    l = list(map(int, input().split()))
    l.sort()

    l_c = [0] * 2001

    for li in l:
        l_c[li] += 1
    for i in range(2000):
        l_c[i + 1] += l_c[i]

    ans = 0

    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            ans += l_c[l[i] + l[j] - 1] - j - 1

    print(ans)


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
