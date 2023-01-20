# 스타트와 링크
# https://www.acmicpc.net/problem/14889
import sys

n = int(sys.stdin.readline())
matrix = []
for _ in range(n):
    matrix.append(list(map(lambda x: int(x), sys.stdin.readline().split())))

# 사람 뽑는 것을 기준으로 시작해야 함.
# 한 팀에는 n//2 명을 뽑음
# n == 4 (3회)
# 1 2 / 1 3 / 1 4 끝.
# n == 6 (10회)
# 1 2 3 / 1 2 4 / 1 2 5 / 1 2 6 / 1 3 4 / 1 3 5 / 1 3 6 / 1 4 5 / 1 4 6 / 1 5 6
people = [0 for _ in range(n//2)]
people[0] = 1

