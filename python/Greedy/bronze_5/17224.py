# 17224 : APC는 왜 서브태스크 대회가 되었을까?
# https://www.acmicpc.net/problem/17224

# 첫 줄 : 문제 개수 N / 역량 L / 해결 문제 개수 K
# 다음 줄 : 쉬운 문제 l / 어려운 문제 l

N, L, K = map(lambda ele: int(ele), input().split(" "))

score = []
for i in range(0, N):
    temp_score = 0
    sub1, sub2 = map(lambda ele: int(ele), input().split(" "))

    if sub1 <= L:
        temp_score += 100

    if sub2 <= L:
        temp_score += 40
    score.append(temp_score)

score.sort(reverse=True)

result = 0
for i in range(0, K):
    result += score[i]

print(result)