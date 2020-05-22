#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


def main():
    input = stdin.readline
    s = list(input()[:-1])[::-1]
    N = len(s)
    p10 = [1]
    tmp = 1
    for _ in range(N - 1):
        tmp = tmp * 10 % 2019
        p10.append(tmp)
    mod = []
    tmp = 0
    for num, p in zip(s, p10):
        tmp = (tmp + int(num) * p) % 2019
        mod.append(tmp)

    mod.sort()
    mod.insert(0, 0)

    ans = 0
    count = 1
    for i in range(1, N + 1):
        if mod[i] == mod[i - 1]:
            count += 1
        else:
            ans += count * (count - 1) // 2
            count = 1
    ans += count * (count - 1) // 2
    print(ans)


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
