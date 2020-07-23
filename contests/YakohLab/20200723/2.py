#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


def main():
    input = stdin.buffer.readline
    s = list(input()[:-1].decode())
    n = len(s)
    ans = 0
    for i in range(n):
        if s[i] == 'U':
            ans += n - i - 1 + 2 * (i)
        else:
            ans += 2 * (n - i - 1) + i

    print(ans)


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
