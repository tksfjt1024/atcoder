from sys import stdin, setrecursionlimit


def main():
    h = int(stdin.readline())

    ans = 0

    while 2 ** (ans + 1) <= h:
        ans += 1

    print(2 ** (ans + 1) - 1)


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
