#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


def main():
    n = int(stdin.readline())
    s = [stdin.readline()[:-1] for _ in range(n)]
    keys = list(set(s))
    keys.sort()
    summary = {}

    for key in keys:
        summary[key] = 0

    m = 0
    for si in s:
        summary[si] += 1
        m = max(summary[si], m)

    for key in keys:
        if summary[key] == m:
            print(key)


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
