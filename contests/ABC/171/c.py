#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


a_list = 'abcdefghijklmnopqrstuvwxyz'


def base_convert(nl, ibase, obase):
    o = []
    while any(nl):
        c = 0
        for i in range(len(nl)):
            c = c * ibase + nl[i]
            nl[i], c = divmod(c, obase)
        o.append(c)
    o.reverse()
    return o


def main():
    input = stdin.buffer.readline
    N = int(input())
    if N == 1:
        print('a')
    else:
        arr = [1]
        tmp = 1
        while arr[-1] <= 1000000000000001:
            tmp *= 26
            arr.append(tmp)
        k = 0
        while N >= arr[k]:
            N -= arr[k]
            k += 1
        n = [int(i) for i in list(str(N))]
        idx = base_convert(n, 10, 26)
        idx = [0] * (k - len(idx)) + idx
        print(*[a_list[i] for i in idx], sep='')


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
