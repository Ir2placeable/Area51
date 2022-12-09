# 2865 : 나는 위대한 슈퍼스타K
# https://www.acmicpc.net/problem/2865

# N : 예선 참가자 수
# M : 장르의 수
# K : 본선 진출자 수
# 참가자는 1개의 장르만 선택 가능
import math

N, M, K = map(lambda x: int(x), input().split(" "))

# people_list 를 미리 만든다.
people_list = []
for i in range(0, N):
    people_list.append(0)

for i in range(0, M):
    temp = list(map(lambda x: float(x), input().split(" ")))

    for j in range(0, len(temp)-1, 2):
        index = int(temp[j]) - 1
        score = temp[j+1]

        # people_list[index].append(score)
        people_list[index] = max(people_list[index], score)
people_list.sort(reverse=True)
# print(people_list)

score_sum = 0
for i in range(0, K):
    score_sum += people_list[i]
print(round(score_sum, 1))