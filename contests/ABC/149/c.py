#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


def main():
    input = stdin.buffer.readline
    x = int(input())

    while True:
        for i in reversed(range(1, x)):
            if i == 1:
                print(x)
                exit()
            elif x % i == 0:
                break
        else:
            continue
        x += 1
        continue


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
