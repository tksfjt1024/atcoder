#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


def find(arr, n):
    arr_2 = sorted(arr)
    for i in range(len(arr_2)):
        if arr_2[i] == n:
            return i


def main():
    input = stdin.buffer.readline
    n = int(input())
    p = list(map(int, input().split()))
    q = list(map(int, input().split()))

    f = [1] * n
    for i in range(n - 1):
        f[i + 1] = f[i] * (i + 2)

    ans_p = 0
    ans_q = 0
    tmp_p = p
    tmp_q = q
    for i in range(n):
        p_i = find(tmp_p, tmp_p[0])
        tmp_p = tmp_p[1:]
        ans_p += p_i * f[len(tmp_p) - 1]
        q_i = find(tmp_q, tmp_q[0])
        tmp_q = tmp_q[1:]
        ans_q += q_i * f[len(tmp_q) - 1]
    print(abs(ans_q - ans_p))


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
