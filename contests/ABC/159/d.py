#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


def main():
    input = stdin.buffer.readline
    n = int(input())
    a = list(map(int, input().split()))

    c_n = []
    for i in range(n + 1):
        c_n.append(i * (i - 1) // 2)

    sorted_a = sorted(a)
    g = {}
    count = 1
    tmp = 0
    for ai in sorted_a:
        if tmp == ai:
            count += 1
        else:
            g[tmp] = count
            count = 1
        tmp = ai
    g[tmp] = count

    ans = 0
    for k in g:
        ans += c_n[g[k]]

    for ai in a:
        print(ans - g[ai] + 1)


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
