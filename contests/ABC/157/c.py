from sys import stdin, setrecursionlimit


def main():
    n, m = map(int, stdin.readline().split())
    sc = [list(map(int, stdin.readline().split())) for _ in range(m)]

    ans = [-1] * n

    for s, c in sc:
        if ans[s - 1] == -1:
            ans[s - 1] = c
        elif ans[s - 1] != c:
            print(-1)
            exit()

    for i in range(n):
        if i == 0 and ans[i] == -1 and n > 1:
            ans[i] = 1
        elif i == 0 and ans[i] == 0 and n > 1:
            print(-1)
            exit()
        elif ans[i] == -1:
            ans[i] = 0
        ans[i] = str(ans[i])

    print(''.join(ans))


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
