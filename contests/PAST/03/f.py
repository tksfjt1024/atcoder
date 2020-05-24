#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


def main():
    input = stdin.readline
    n = int(input())
    a = [set(list(input()[:-1])) for _ in range(n)]
    ans = []
    for i in range(n // 2):
        common = a[i] & a[n - i - 1]
        if len(common) > 0:
            common = list(common)
            ans.append(common[0])
        else:
            print(-1)
            exit()

    if len(ans) == 0 and n > 1:
        print(-1)
    elif n % 2 == 0:
        print(*ans, *reversed(ans), sep='')
    else:
        print(*ans, list(a[n // 2])[0], *reversed(ans), sep='')


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
