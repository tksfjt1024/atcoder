from sys import stdin, setrecursionlimit


def main():
    a, b, c = map(int, stdin.readline().split())
    print('Yes') if 3 - len(set([a, b, c])) == 1 else print('No')


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
