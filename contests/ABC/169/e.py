#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


def main():
    input = stdin.buffer.readline
    n = int(input())
    ab = [list(map(int, input().split())) for _ in range(n)]
    min_arr = sorted(ab, key=lambda x: x[0])
    max_arr = sorted(ab, key=lambda x: x[1])
    if n % 2 != 0:
        a = min_arr[n // 2][0]
        b = max_arr[n // 2][1]
        print(b - a + 1)
    else:
        a1 = min_arr[(n - 1) // 2][0]
        b1 = max_arr[(n - 1) // 2][1]
        a2 = min_arr[(n + 1) // 2][0]
        b2 = max_arr[(n + 1) // 2][1]
        print(b1 + b2 - a1 - a2 + 1)


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
