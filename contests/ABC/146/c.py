#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


def main():
    input = stdin.buffer.readline
    a, b, x = map(int, input().split())

    max = 0
    ans = 0

    for d in range(1, 11):
        tmp = (x - b * d) // a
        if max < a * tmp + b * d and 10 ** (d - 1) <= tmp < 10 ** d:
            max = a * tmp + b * d
            ans = tmp
        if max < a * (10 ** d - 1) + b * d <= x:
            max = a * (10 ** d - 1) + b * d
            ans = 10 ** d - 1

    if ans > 10 ** 9:
        print(10 ** 9)
    else:
        print(ans)


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
