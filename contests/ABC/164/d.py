#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


def main():
    mod = 2019
    input = stdin.buffer.readline
    s = list(map(int, list(input()[:-1].decode())))
    n = len(s)
    s.reverse()

    tmp_p10 = 1
    p10 = [tmp_p10]
    for _ in range(1, n + 1):
        tmp_p10 *= 10
        tmp_p10 %= mod
        p10.append(tmp_p10)

    tmp_mod = s[0] % mod
    mods = [0, tmp_mod]
    for i in range(1, n):
        tmp_mod = (s[i] * p10[i] + tmp_mod) % mod
        mods.append(tmp_mod)
    m2019 = [0] * 2019
    for mi in mods:
        m2019[mi] += 1
    ans = 0
    for mi in m2019:
        ans += mi * (mi - 1) // 2

    print(ans)


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
