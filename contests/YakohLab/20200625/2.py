#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


def main():
    input = stdin.buffer.readline
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    arr = [ai - bi for ai, bi in zip(a, b)]
    arr.sort(reverse=True)
    tmp_1 = sum([-ai for ai in arr if ai < 0])
    tmp_2 = sum([ai for ai in arr if ai > 0])
    ans = 0
    for ai in arr:
        if ai < 0:
            ans += 1
    if tmp_2 < tmp_1:
        print(-1)
    else:
        for ai in arr:
            if ai > 0:
                if tmp_1 > 0:
                    tmp_1 -= ai
                    ans += 1

        print(ans)


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
