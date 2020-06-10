#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


def main():
    input = stdin.buffer.readline
    n, m = map(int, input().split())
    q = [list(map(int, input().split())) for _ in range(m)]
    p = list(map(int, input().split()))

    ans = 0
    for i in range(1 << n):
        check = True
        for j in range(m):
            ki = q[j][0]
            tmp_c = 0
            for k in range(1, ki + 1):
                if i & (1 << (q[j][k] - 1)):
                    tmp_c += 1
            if tmp_c % 2 != p[j]:
                check = False
                break
        if check:
            ans += 1
    print(ans)


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
