# 22864 : 피로도
# https://www.acmicpc.net/problem/22864

# 하루는 24시간
# a : 시간당 피로도 누적치
# b : 시간당 작업 누적치
# c : 시간당 피로도 감소치
# m : 최대 피로도
a, b, c, m = map(lambda ele: int(ele), input().split(" "))

works = 0
fatigue = 0
# 매 시간 반복
for hour in range(0, 24):
    # 피로도가 남아있으면
    if fatigue + a <= m:
        fatigue += a
        works += b
    # 피로도가 부족하면
    else:
        fatigue = max(0, fatigue-c)

print(works)