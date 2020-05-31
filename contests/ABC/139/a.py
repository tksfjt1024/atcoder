#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


def main():
    input = stdin.buffer.readline
    s = list(input()[:-1].decode())
    t = list(input()[:-1].decode())

    ans = 0

    for i in range(3):
        if s[i] == t[i]:
            ans += 1

    print(ans)


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
