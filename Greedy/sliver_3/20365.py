# 20365 : 블로그2
# https://www.acmicpc.net/problem/20365
import sys

n = int(sys.stdin.readline())
problems = sys.stdin.readline().rstrip()

prev = problems[0]
b, r = 0, 0
for problem in problems:
    if prev == problem:
        continue

    if problem == 'R':
        b += 1
    elif problem == 'B':
        r += 1
    prev = problem

if problem[-1] == 'R':
    r += 1
elif problem[-1] == 'B':
    b += 1

print(min(b, r) + 1)