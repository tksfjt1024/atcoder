#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


def main():
    input = stdin.buffer.readline
    a = int(input())
    b = int(input())
    print(*(set([1, 2, 3]) - set([a]) - set([b])))


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
