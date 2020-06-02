#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


def main():
    input = stdin.buffer.readline
    n = int(input())
    s = [''.join(sorted(list(input()[:-1].decode()))) for _ in range(n)]

    nc2 = [i * (i - 1) // 2 for i in range(10 ** 5 + 1)]

    summary = {}

    for si in s:
        if si in summary:
            summary[si] += 1
        else:
            summary[si] = 1

    ans = 0

    for si in summary:
        ans += nc2[summary[si]]

    print(ans)


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
