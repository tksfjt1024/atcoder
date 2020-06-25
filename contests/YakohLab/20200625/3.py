#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


def main():
    input = stdin.buffer.readline
    n = int(input())
    ab = [list(map(int, input().split())) for _ in range(n)]
    for i in range(n):
        ab[i].append(ab[i][0] + ab[i][1])
    arr = sorted(ab, reverse=True, key=lambda x: x[2])
    ans = 0
    for i in range(n):
        if i % 2 == 0:
            ans += arr[i][0]
        else:
            ans -= arr[i][1]
    print(ans)


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
