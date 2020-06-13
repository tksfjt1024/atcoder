#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


def main():
    input = stdin.buffer.readline
    s = input()[:-1].decode()
    print(s[:3])


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
