# 25176 : 청정수열
# https://www.acmicpc.net/problem/25176

# 첫 줄 : 2N = input
# 값이 최소인 청정수열의 개수를 구하라

n = int(input())

result = 1
for i in range(1, n+1):
    result *= i
print(result)
