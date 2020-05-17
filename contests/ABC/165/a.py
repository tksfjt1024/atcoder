#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


def main():
    input = stdin.buffer.readline
    k = int(input())
    a, b = map(int, input().split())
    for i in range(a, b + 1):
        if i % k == 0:
            print('OK')
            exit()
    print('NG')


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
