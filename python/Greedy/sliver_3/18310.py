# 18310 : 안테나
# https://www.acmicpc.net/problem/18310

n = int(input())
home_list = list(map(lambda x: int(x), input().split(" ")))
home_list.sort()
print(home_list[(n-1)//2])