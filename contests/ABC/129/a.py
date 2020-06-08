#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


def main():
    input = stdin.buffer.readline
    p, q, r = map(int, input().split())
    print(sum([p, q, r]) - max(p, q, r))


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
