#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


def main():
    input = stdin.buffer.readline
    n, k = map(int, input().split())
    r, s, p = map(int, input().split())
    t = input()[:-1].decode()

    ans = 0
    result = [False] * n
    for i in range(n):
        if k <= i and t[i] == t[i - k] and result[i - k]:
            continue
        if t[i] == 'r':
            ans += p
        elif t[i] == 's':
            ans += r
        elif t[i] == 'p':
            ans += s
        result[i] = True

    print(ans)


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
