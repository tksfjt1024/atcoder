#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


def main():
    input = stdin.buffer.readline
    s = list(input()[:-1].decode())
    words = []
    word = [s[0]]
    for i in range(1, len(s)):
        if s[i].isupper() and s[i - 1].isupper() and len(word) > 1:
            words.append(''.join(word))
            word = [s[i]]
        else:
            word.append(s[i])
    words.append(''.join(word))
    words.sort(key=lambda s: s.lower())
    print(*words, sep='')


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
