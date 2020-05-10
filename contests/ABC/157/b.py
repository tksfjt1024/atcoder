from sys import stdin, setrecursionlimit


def main():
    a = [list(map(int, stdin.readline().split())) for _ in range(3)]
    n = int(stdin.readline())
    b = [int(stdin.readline()) for _ in range(n)]

    bg = []
    for i in range(3):
        bg.append(a[i])
        bg.append([a[0][i], a[1][i], a[2][i]])
    bg.append([a[i][i] for i in range(3)])
    bg.append([a[i][2 - i] for i in range(3)])

    for bgi in bg:
        if len(list(set(bgi) - set(b))) == 0:
            print('Yes')
            exit()

    print('No')


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
