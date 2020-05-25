#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


def main():
    input = stdin.buffer.readline
    n = int(input())
    s = list(input()[:-1].decode())
    pre_si = s[0]
    s2 = [pre_si]
    for i in range(1, n):
        if s[i] != pre_si:
            s2.append(s[i])
            pre_si = s[i]

    print(len(s2))


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
