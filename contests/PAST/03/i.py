#!/usr/bin/env python3

from sys import stdin, setrecursionlimit
from copy import copy


def main():
    input = stdin.buffer.readline
    n = int(input())
    q = int(input())
    queries = [list(map(int, input().split())) for _ in range(q)]

    a = [[n * i + j for j in range(n)] for i in range(n)]

    seq = [i for i in range(n)]

    c_indexes = copy(seq)
    r_indexes = copy(seq)
    t_count = 0
    check = False

    for query in queries:
        if query[0] == 1:
            check = True
            i = query[1] - 1
            j = query[2] - 1
            if t_count % 2 == 0:
                tmp_i = r_indexes[i]
                tmp_j = r_indexes[j]
                r_indexes[i] = tmp_j
                r_indexes[j] = tmp_i
            else:
                tmp_i = c_indexes[i]
                tmp_j = c_indexes[j]
                c_indexes[i] = tmp_j
                c_indexes[j] = tmp_i
        elif query[0] == 2:
            check = True
            i = query[1] - 1
            j = query[2] - 1
            if t_count % 2 == 0:
                tmp_i = c_indexes[i]
                tmp_j = c_indexes[j]
                c_indexes[i] = tmp_j
                c_indexes[j] = tmp_i
            else:
                tmp_i = r_indexes[i]
                tmp_j = r_indexes[j]
                r_indexes[i] = tmp_j
                r_indexes[j] = tmp_i
        elif query[0] == 3:
            check = True
            t_count += 1
        elif query[0] == 4:
            if check:
                if t_count % 2 != 0:
                    a = [[a[j][i] for j in c_indexes] for i in r_indexes]
                else:
                    a = [[a[i][j] for j in c_indexes] for i in r_indexes]

            i = query[1] - 1
            j = query[2] - 1
            print(a[i][j])
            c_indexes = copy(seq)
            r_indexes = copy(seq)
            t_count = 0
            check = False


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
