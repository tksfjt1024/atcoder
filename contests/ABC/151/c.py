from sys import stdin, setrecursionlimit


def main():
    n, m = map(int, stdin.readline().split())
    ac = [0] * n
    wa = [0] * n
    for _ in range(m):
        p, s = map(str, stdin.readline().split())
        p = int(p) - 1
        if ac[p] == 0 and s == 'WA':
            wa[p] += 1
        elif s == 'AC':
            ac[p] = 1
    n_ac = 0
    n_wa = 0
    for i in range(n):
        n_ac += ac[i]
        if ac[i] == 1:
            n_wa += wa[i]

    print(n_ac, n_wa)


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
