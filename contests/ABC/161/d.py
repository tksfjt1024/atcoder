#!/usr/bin/env python3

from sys import stdin, setrecursionlimit
from collections import deque


def main():
    input = stdin.buffer.readline
    k = int(input())
    count = 0
    q = deque()
    for i in range(1, 10):
        q.append(str(i))
    while True:
        qi = q.popleft()
        last = int(qi[-1])
        if last != 0:
            q.append(qi + str(last - 1))
        q.append(qi + str(last))
        if last != 9:
            q.append(qi + str(last + 1))
        count += 1
        if count == k:
            print(qi)
            break


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
