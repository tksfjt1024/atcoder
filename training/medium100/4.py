#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


def main():
    input = stdin.buffer.readline
    s = list(input()[:-1].decode())
    n = len(s)
    for i in reversed(range(n - 1)):
        if (i + 1) % 2 == 0:
            l = ''.join(s[:(i + 1) // 2])
            r = ''.join(s[(i + 1) // 2:i + 1])
            if l == r:
                print(i + 1)
                exit()


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
