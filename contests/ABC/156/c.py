#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


def main():
    input = stdin.buffer.readline
    n = int(input())
    x = list(map(int, input().split()))
    sum = 0
    for xi in x:
        sum += xi
    ans_1 = sum // n
    ans_2 = sum // n + 1
    score_1 = 0
    score_2 = 0
    for xi in x:
        score_1 += (xi - ans_1) ** 2
        score_2 += (xi - ans_2) ** 2
    print(min(score_1, score_2))


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
