#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


def main():
    c = stdin.readline()[:-1]
    print(chr(ord(c) + 1))


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
