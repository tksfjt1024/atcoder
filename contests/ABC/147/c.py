#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


def main():
    input = stdin.buffer.readline
    n = int(input())
    xy = []
    for _ in range(n):
        ai = int(input())
        xyi = [list(map(int, input().split())) for _ in range(ai)]
        xy.append(xyi)

    ans = 0
    flag = False

    for i in range(1 << n):
        for j in range(n):
            if i & (1 << j):
                for x, y in xy[j]:
                    if y == 1:
                        if not i & (1 << (x - 1)):
                            flag = True
                    if y == 0:
                        if i & (1 << (x - 1)):
                            flag = True
        if not flag:
            tmp = 0
            for j in range(n):
                if i & (1 << j):
                    tmp += 1
            if ans < tmp:
                ans = tmp
        flag = False

    print(ans)


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
