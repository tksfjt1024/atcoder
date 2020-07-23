#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


class UnionFindTree:
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        p = self.parents
        while p[x] >= 0:
            x, p[x] = p[x], p[p[x]]
        return x

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        p = self.parents
        if x != y:
            if x > y:
                x, y = y, x
            p[x], p[y] = p[x] + p[y], x

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def size(self, x):
        return - self.parents[self.find(x)]

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())


def main():
    input = stdin.buffer.readline
    n, k, l = map(int, input().split())

    fk = UnionFindTree(n)
    for _ in range(k):
        p, q = map(int, input().split())
        fk.union(p - 1, q - 1)

    fl = UnionFindTree(n)
    for _ in range(l):
        r, s = map(int, input().split())
        fl.union(r - 1, s - 1)

    ans = []
    roots_k = fk.roots()
    roots_l = fl.roots()

    members_k = [fk.members(i) for i in roots_k]
    members_l = [fl.members(i) for i in roots_l]
    for i in range(n):
        ans.append(len(set(members_k[roots_k.index(fk.find(i))]) & set(members_l[roots_l.index(fl.find(i))])))

    print(*ans)


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
