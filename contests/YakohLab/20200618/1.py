#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


def main():
    input = stdin.readline
    n = int(input())
    s_arr = []
    t_arr = []
    for _ in range(n):
        s, t = list(map(str, input().split()))
        t = int(t)
        s_arr.append(s)
        t_arr.append(t)
    x = input()[:-1]
    print(sum(t_arr[s_arr.index(x) + 1:]))


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
