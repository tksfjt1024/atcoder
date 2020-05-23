#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


def main():
    input = stdin.buffer.readline
    n = int(input())

    pre_a = int(input())

    for _ in range(1, n):
        ai = int(input())
        if ai == pre_a:
            print('stay')
        elif ai < pre_a:
            print('down', pre_a - ai)
        elif ai > pre_a:
            print('up', ai - pre_a)
        pre_a = ai


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
