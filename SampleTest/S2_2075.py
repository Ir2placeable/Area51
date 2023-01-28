# https://www.acmicpc.net/problem/2075

# 그냥 힙으로 정렬하면 되는거 아닌가? -> 메모리 초과
# 한 줄씩 일단 받고, 그 줄에서 제일 큰 수를 따로 저장해둠

import sys

n = int(sys.stdin.readline())
queue = []

for _ in range(n):
    print(sorted(list(map(lambda x: int(x), sys.stdin.readline().split()))))
