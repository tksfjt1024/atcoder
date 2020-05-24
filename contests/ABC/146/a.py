#!/usr/bin/env python3

from sys import stdin, setrecursionlimit

WEEK = {
    'SUN': 0,
    'MON': 1,
    'TUE': 2,
    'WED': 3,
    'THU': 4,
    'FRI': 5,
    'SAT': 6
}


def main():
    input = stdin.buffer.readline
    s = input()[:-1].decode()
    print(7 - WEEK[s])


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
