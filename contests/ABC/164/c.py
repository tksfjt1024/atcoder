#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


def main():
    input = stdin.buffer.readline
    n = int(input())
    items = set()
    for _ in range(n):
        items.add(input()[:-1])
    print(len(items))


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
