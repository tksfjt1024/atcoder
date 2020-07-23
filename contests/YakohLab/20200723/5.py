#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


def main():
    input = stdin.buffer.readline
    n = int(input())
    ta = [list(map(int, input().split())) for _ in range(n)]
    ans = sum(ta[0])
    for i in range(1, n):
        si1 = sum(ta[i - 1])
        si = sum(ta[i])
        cand1 = (ans * ta[i - 1][0] // si1) // ta[i][0] if (ans * ta[i - 1][0] // si1) % ta[i][0] == 0 else (ans * ta[i - 1][0] // si1) // ta[i][0] + 1
        cand2 = (ans * ta[i - 1][1] // si1) // ta[i][1] if (ans * ta[i - 1][1] // si1) % ta[i][1] == 0 else (ans * ta[i - 1][1] // si1) // ta[i][1] + 1
        ans = si * max([cand1, cand2])
    print(ans)


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
