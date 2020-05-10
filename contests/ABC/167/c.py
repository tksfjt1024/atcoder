#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


def main():
    input = stdin.buffer.readline
    n, m, x = map(int, input().split())
    ca = [list(map(int, input().split())) for _ in range(n)]
    min_ans = 10 ** 20
    max_count = 0
    for i in range(2 ** n):
        ii = list(format(i, 'b').zfill(n))
        sum_a = [0] * m
        ans = 0
        for j in range(n):
            if ii[j] == '1':
                c, *a = ca[j]
                ans += c
                for k in range(m):
                    sum_a[k] += a[k]
        check = True
        for j in range(m):
            if sum_a[j] < x:
                check = False
        if check and min_ans > ans:
            min_ans = ans

    if min_ans == 10 ** 20:
        print(-1)
    else:
        print(min_ans)


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
