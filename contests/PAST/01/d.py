#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


def main():
    input = stdin.buffer.readline
    n = int(input())
    arr = {i for i in range(1, n + 1)}
    for i in range(n):
        ai = int(input())
        try:
            arr.remove(ai)
        except:
            ans_1 = ai
    ans_2 = int(*arr)
    try:
        print(ans_1, ans_2)
    except:
        print('Correct')


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
