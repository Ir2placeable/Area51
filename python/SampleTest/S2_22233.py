# https://www.acmicpc.net/problem/22233

# 집합 문제인 것으로 보인다. -> defaultdict 이용

import sys
from collections import defaultdict

n, m = map(lambda x: int(x), sys.stdin.readline().split())
keywords = defaultdict(int)
for _ in range(n):
    word = sys.stdin.readline().strip()
    keywords[word] = 1


for _ in range(m):
    words = list(sys.stdin.readline().rstrip().split(","))
    for word in words:
        keywords[word] -= 1

        if keywords[word] <= 0:
            del keywords[word]
    print(len(keywords))