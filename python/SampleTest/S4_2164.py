# https://www.acmicpc.net/problem/2164

# 간단한 deque 사용문제
from collections import deque
import sys

n = int(sys.stdin.readline())
cards = deque([i for i in range(1, n+1)])

while len(cards) > 1:
    cards.popleft()
    cards.append(cards.popleft())
print(cards.popleft())