#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


def main():
    input = stdin.buffer.readline
    n, q = map(int, input().split())
    f = [0 for _ in range(n)]
    for _ in range(q):
        s = list(map(int, input().split()))

        if s[0] == 1:
            a, b = s[1] - 1, s[2] - 1
            f[a] = f[a] | (1 << b)
        elif s[0] == 2:
            a = s[1] - 1
            for i in range(n):
                if i != a and f[i] & (1 << a):
                    f[a] = f[a] | (1 << i)
        elif s[0] == 3:
            a = s[1] - 1
            candidates = []
            for i in range(n):
                if i != a and f[a] & (1 << i):
                    candidates.append(i)
            for c in candidates:
                f[a] = f[a] | f[c]

    for i in range(n):
        ans = []
        for j in range(n):
            if i != j and f[i] & (1 << j):
                ans.append('Y')
            else:
                ans.append('N')
        print(*ans, sep='')


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
