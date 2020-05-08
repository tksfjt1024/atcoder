from sys import stdin, setrecursionlimit


def main():
    h, n = map(int, stdin.readline().split())
    a = list(map(int, stdin.readline().split()))
    print('Yes') if sum(a) >= h else print('No')


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
