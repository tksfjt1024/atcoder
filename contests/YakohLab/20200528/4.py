#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


def main():
    input = stdin.buffer.readline
    n, k = map(int, input().split())
    v = list(map(int, input().split()))

    max = 0

    for i in range(k):
        if i <= n:
            for j in range(i + 1):
                candidate = v[0:j + 1]
                candidate.extend(v[n - i + j:n])
                candidate.sort()
                for d in range(k - i):
                    tmp = sum(candidate[d:n])
                    if tmp > max:
                        max = tmp
        else:
            candidate = v
            candidate.sort()
            for d in range(k - i):
                tmp = sum(candidate[d:n])
                if tmp > max:
                    max = tmp
    print(max)


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
