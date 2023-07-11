# 21758 : 꿀 따기
# https://www.acmicpc.net/problem/21758

n = int(input())
flowers = list(map(lambda x: int(x), input().split(" ")))

max_honey = 0
# 벌통 중간
default_honey = sum(flowers) - flowers[0] - flowers[-1]
for i in range(1, n-1):
    temp_honey = default_honey + flowers[i]
    max_honey = max(max_honey, temp_honey)
# print(max_honey)

# 벌통 오른쪽 고정
default_honey = sum(flowers[1:]) * 2
lost_honey = 0
for i in range(1, n-1):
    lost_honey += flowers[i]
    temp_honey = default_honey - lost_honey - flowers[i]
    max_honey = max(max_honey, temp_honey)
# print(max_honey)

# 벌통 왼쪽 고정
flowers.reverse()
default_honey = sum(flowers[1:]) * 2
lost_honey = 0
for i in range(1, n-1):
    lost_honey += flowers[i]
    temp_honey = default_honey - lost_honey - flowers[i]
    max_honey = max(max_honey, temp_honey)
print(max_honey)