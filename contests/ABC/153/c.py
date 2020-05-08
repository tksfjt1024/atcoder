from sys import stdin, setrecursionlimit


def main():
    n, k = map(int, stdin.readline().split())
    h = list(map(int, stdin.readline().split()))
    h.sort()

    ans = 0
    for i in range(n - k):
        ans += h[i]
    print(ans)


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
