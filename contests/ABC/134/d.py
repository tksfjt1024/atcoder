#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


def main():
    input = stdin.buffer.readline
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] * n
    for i in range(n):
        mod = n - i
        x = 1
        tmp = 0
        while x * mod <= n:
            tmp += b[x * mod - 1]
            x += 1
        if tmp % 2 != a[mod - 1]:
            b[mod - 1] = 1

    ans_m = 0
    ans_b = []
    for i in range(n):
        if b[i] > 0:
            ans_m += 1
            ans_b.append(i + 1)
    print(ans_m)
    if len(ans_b) > 0:
        print(*ans_b)


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
