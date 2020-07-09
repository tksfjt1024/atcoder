#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


def main():
    input = stdin.buffer.readline
    n, m = map(int, input().split())
    red = [False] * n
    red[0] = True
    balls = [1] * n
    ans = 1
    for _ in range(m):
        x, y = map(int, input().split())
        if red[x - 1]:
            if balls[x - 1] == 1:
                red[x - 1] = False
                ans -= 1
            if not red[y - 1]:
                red[y - 1] = True
                ans += 1
        balls[x - 1] -= 1
        balls[y - 1] += 1
    print(ans)


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
