# 19941 : 햄버거 분배
# https://www.acmicpc.net/problem/19941
import sys

n, fork = map(lambda x: int(x), sys.stdin.readline().split(" "))
temp = sys.stdin.readline().rstrip()
table = []
for char in temp:
    table.append(char)

val = 0
for i in range(0, n):
    if table[i] == 'H':
        for j in range(max(0, i-fork), min(n, i+fork+1), 1):
            if table[j] == 'P':
                val += 1
                table[j] = 'X'
                break
print(val)