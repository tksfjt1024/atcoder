#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


def main():
    input = stdin.buffer.readline
    W, H, x, y = map(int, input().split())
    if W == 2 * x and H == 2 * y:
        print(W * H / 2, 1)
    else:
        print(W * H / 2, 0)


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
