#!/usr/bin/env python3

from sys import stdin, setrecursionlimit
from collections import deque


def main():
    input = stdin.buffer.readline
    n = int(input())
    d = list(map(int, input().split()))
    m = int(input())
    t = list(map(int, input().split()))
    if m > n:
        print('NO')
    else:
        d.sort()
        t.sort()
        dq = deque(d)
        tq = deque(t)
        while tq:
            ti = tq.popleft()
            di = dq.popleft()
            while di < ti:
                di = dq.popleft()
            if di > ti:
                print('NO')
                exit()
        print('YES')


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
