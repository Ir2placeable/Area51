# 20937 : 떡국
# https://www.acmicpc.net/problem/20937

n = int(input())
items = list(map(lambda x: int(x), input().split(" ")))

dic = {}
for item in items:
    if item in dic:
        dic[item] += 1
    else:
        dic[item] = 1

print(sorted(dic.items(), key=lambda x: x[1], reverse=True)[0][1])