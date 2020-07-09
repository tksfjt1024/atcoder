#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


def factorization(n):
    arr = {}
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp % i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                temp //= i
            arr[i] = cnt

    if temp != 1:
        arr[temp] = 1

    if arr == []:
        arr[n] = 1

    return arr


def main():
    input = stdin.buffer.readline
    n, p = map(int, input().split())
    f = factorization(p)
    ans = 1
    for k in f:
        if f[k] >= n:
            ans *= k ** (f[k] // n)
    print(ans)


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
