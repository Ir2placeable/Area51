# 15886 : 내 선물을 받아줘 2
# https://www.acmicpc.net/problem/15886

n = int(input())
string = input()

count = 0
for i in range(0, n-1):
    if string[i] + string[i+1] == 'EW':
        count += 1

print(count)