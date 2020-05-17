#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


def check(n, k):
    tmp = n
    while tmp % k == 0:
        tmp = tmp // k
    return tmp % k == 1


def main():
    input = stdin.buffer.readline
    n = int(input())
    ans = 1
    if n > 2:
        ans += 1
    for i in range(2, int((n - 1) ** 0.5) + 1):
        if (n - 1) % i == 0:
            ans += 1
            if i != (n - 1) // i:
                ans += 1
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            if check(n, i):
                ans += 1
            if check(n, n // i) and i != n // i:
                ans += 1
    print(ans)


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
