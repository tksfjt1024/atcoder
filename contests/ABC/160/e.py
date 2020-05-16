#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


def main():
    input = stdin.buffer.readline
    x, y, a, b, c = map(int, input().split())
    pqr = []
    p = list(map(int, input().split()))
    q = list(map(int, input().split()))
    r = list(map(int, input().split()))
    for i in range(a):
        pqr.append([p[i], 1])
    for i in range(b):
        pqr.append([q[i], 2])
    for i in range(c):
        pqr.append([r[i], 0])
    pqr.sort(reverse=True)

    ans = 0
    c_a = 0
    c_b = 0
    c_c = 0
    for v, k in pqr:
        if k == 1 and c_a < x:
            ans += v
            c_a += 1
        elif k == 2 and c_b < y:
            ans += v
            c_b += 1
        elif k == 0 and c_a + c_b + c_c < x + y:
            ans += v
            c_c += 1
        if c_a + c_b + c_c == x + y:
            print(ans)
            exit()


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
