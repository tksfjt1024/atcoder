#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


def main():
    input = stdin.buffer.readline
    s = list(input()[:-1].decode())
    n = len(s)
    ans = [0] * n

    tmp_r_count = tmp_l_count = 1
    tmp_index = 0
    for i in range(1, n):
        if s[i - 1] == s[i] == 'R':
            tmp_r_count += 1
        elif s[i - 1] == s[i] == 'L':
            tmp_l_count += 1
        elif s[i - 1] == 'R' and s[i] == 'L':
            tmp_index = i - 1
        elif s[i - 1] == 'L' and s[i] == 'R':
            ans[tmp_index] += (tmp_r_count + 1) // 2 + tmp_l_count // 2
            ans[tmp_index + 1] += tmp_r_count // 2 + (tmp_l_count + 1) // 2
            tmp_r_count = tmp_l_count = 1

    ans[tmp_index] += (tmp_r_count + 1) // 2 + tmp_l_count // 2
    ans[tmp_index + 1] += tmp_r_count // 2 + (tmp_l_count + 1) // 2

    print(*ans)


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
