# 14655 : 욱제는 도박쟁이야!!
# https://www.acmicpc.net/problem/14655

# 첫 줄 : 동전의 개수
# 두번째 줄 : 합이 최대
# 세번째 줄 : 합이 최소
# 점수 : round1 - round2
coins = int(input())

round1 = list(map(lambda ele: int(ele), input().split(" ")))
round2 = list(map(lambda ele: int(ele), input().split(" ")))

score = 0
for i in range(0, coins):
    score += max(round1[i], -1 * round1[i])
    score -= min(round2[i], -1 * round2[i])

print(score)
