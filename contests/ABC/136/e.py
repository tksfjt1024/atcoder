#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


def main():
    input = stdin.buffer.readline
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    s = sum(a)
    cand = [s]
    for i in range(2, int(s ** 0.5) + 1):
        if s % i == 0:
            cand.append(i)
            cand.append(s // i)
    cand.sort(reverse=True)

    for c in cand:
        arr = [a[i] % c for i in range(n)]
        arr.sort()
        sum_r = [0] * n
        sum_r[0] = arr[0]
        for i in range(1, n):
            sum_r[i] = sum_r[i - 1] + arr[i]
        for i in range(n - 1):
            if sum_r[i] <= k:
                sum_l = c * (n - i - 1) - sum_r[-1] + sum_r[i]
                if sum_r[i] == sum_l:
                    print(c)
                    exit()

    print(1)


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
