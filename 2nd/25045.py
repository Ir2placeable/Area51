# 각 고객 기업에 렌탈해 줄 물품을 잘 정해서 고객 만족도의 합을 최대
import sys

n, m = map(lambda x: int(x), sys.stdin.readline().split())
products = list(map(lambda x: int(x), sys.stdin.readline().split()))
costs = list(map(lambda x: int(x), sys.stdin.readline().split()))

expectation = 0

products.sort(reverse=True)
costs.sort()

for i in range(min(n, m)):
    if products[i] <= costs[i]:
        continue

    expectation += products[i] - costs[i]

print(expectation)