#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


def main():
    input = stdin.buffer.readline
    l, r = map(int, input().split())
    if r - l >= 2019:
        print(0)
    else:
        mods = []
        for i in range(l, r + 1):
            mods.append(i % 2019)
        ans = float('inf')
        for i in range(len(mods) - 1):
            for j in range(i + 1, len(mods)):
                tmp = (mods[i] * mods[j]) % 2019
                if tmp < ans:
                    ans = tmp
        print(ans)


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
