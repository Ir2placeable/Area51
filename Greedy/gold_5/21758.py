# 21758 : 꿀 따기
# https://www.acmicpc.net/problem/21758

# 모든 수를 더한다.
#
n = int(input())
items = list(map(lambda x: int(x), input().split(" ")))

max_val = 0

# 벌통 중간
for mid in range(1, n-1):
    left = sum(items[1:mid+1])
    right = sum(items[mid:n-1])
    # print(a,b,mid)
    max_val = left + right

# 벌통 맨 마지막
default_val = sum(items[1:])
for i in range(1, n-1):
    additional_val = sum(items[i+1:]) - items[i]
    max_val = max(max_val, default_val + additional_val)

# 벌통 맨 앞
default_val = sum(items[:n-1])
for i in range(1, n-1):
    additional_val = sum(items[:i]) - items[i]
    max_val = max(max_val, default_val + additional_val)

print(max_val)
