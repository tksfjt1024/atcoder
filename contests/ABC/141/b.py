#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


def main():
    input = stdin.buffer.readline
    s = list(input()[:-1].decode())
    for i in range(len(s)):
        if i % 2 == 0:
            if not s[i] in ['R', 'U', 'D']:
                print('No')
                exit()
        else:
            if not s[i] in ['L', 'U', 'D']:
                print('No')
                exit()
    print('Yes')


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
