#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


def main():
    input = stdin.buffer.readline
    n = int(input())
    s = list(input()[:-1].decode())
    r = []
    g = []
    b = [0] * n
    len_b = 0
    for i in range(n):
        if s[i] == 'R':
            r.append(i)
        elif s[i] == 'G':
            g.append(i)
        elif s[i] == 'B':
            b[i] = 1
            len_b += 1
    ans = len(r) * len(g) * len_b

    def check(i):
        return 0 <= i < n and b[i] == 1

    for ri in r:
        for gi in g:
            if check(2 * gi - ri):
                ans -= 1
            if check(2 * ri - gi):
                ans -= 1
            if (ri + gi) % 2 == 0 and check((ri + gi) // 2):
                ans -= 1
    print(ans)


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
