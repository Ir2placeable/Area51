# 1789 : 수들의 합
# https://www.acmicpc.net/problem/1789

# 서로 다른 N개의 자연수의 합이 S라고 한다. S를 알 때, 자연수 N의 최댓값은 얼마일까?
# input : S
# output : N의 최댓값 -> 1부터 더한다.

S = int(input())

num = 1

while S >= num:
    S -= num
    num += 1
print(num-1)