#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


def main():
    input = stdin.buffer.readline
    s = list(input()[:-1].decode())
    n = len(s) + 1
    arr = [0] * n
    for i in range(n - 1):
        if s[i] == '<':
            arr[i + 1] = arr[i] + 1
        else:
            arr[i + 1] = 0
    for i in reversed(range(n - 1)):
        if s[i] == '>':
            arr[i] = max(arr[i], arr[i + 1] + 1)

    print(sum(arr))


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
