#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


def main():
    input = stdin.readline
    s = list(input()[:-1])
    t = list(input()[:-1])
    N = len(s)
    S = {}
    T = {}
    t_si = 0
    t_ti = 0
    n_s = []
    n_t = []
    for si, ti in zip(s, t):
        if not si in S:
            S[si] = t_si
            n_s.append(t_si)
            t_si += 1
        else:
            n_s.append(S[si])
        if not ti in T:
            T[ti] = t_ti
            n_t.append(t_ti)
            t_ti += 1
        else:
            n_t.append(T[ti])

    for si, ti in zip(n_s, n_t):
        if si != ti:
            print('No')
            exit()
    print('Yes')


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
