# 1105 : 팔
# https://www.acmicpc.net/problem/1105

# 관건은 L의 자릿수가 넘어 가느냐를 판단해야 함
# ex) 880 -> 900
import sys

L, R = sys.stdin.readline().rstrip().split(" ")

L_list, R_list = [0] * len(R), [0] * len(R)
for i in L:
    L_list.append(i)
for r in R:
    R_list.append(r)

print(L_list, R_list)