#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


def main():
    input = stdin.buffer.readline
    n = int(input())
    s = input()[:-1].decode()

    ans = ''

    for si in s:
        ans += chr(ord('A') + (ord(si) - ord('A') + n) % 26)

    print(ans)


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
