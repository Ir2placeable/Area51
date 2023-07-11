# https://www.acmicpc.net/problem/20920

# 정렬 구현하는 문제인듯
import sys
from collections import defaultdict

n, m = map(lambda x: int(x), sys.stdin.readline().split())
words = defaultdict(int)
for _ in range(n):
    word = sys.stdin.readline().rstrip()
    if len(word) < m:
        continue

    words[word] -= 1

words = sorted(words.items(), key=lambda x: (x[1], -1*len(x[0]), x[0]))
for word, _ in words:
    print(word)