from sys import stdin, setrecursionlimit


def main():
    n = int(stdin.readline())
    print(n // 2) if n % 2 == 0 else print((n + 1) // 2)


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
