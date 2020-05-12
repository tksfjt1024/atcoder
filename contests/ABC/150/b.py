#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


def main():
    input = stdin.buffer.readline
    n = int(input())
    s = list(input()[:-1])
    abc = list('ABC'.encode())
    ans = 0
    for i in range(n - 2):
        if s[i: i + 3] == abc:
            ans += 1
    print(ans)


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
