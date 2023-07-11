# 문제 첫 인상 : 경로탐색 문제처럼 보였음. 그러나 문제조건에서 변수의 범위가 매우 크게 제시됨.
# 경로탐색 알고리즘은 모든 경로를 돌기 때문에, 해당 알고리즘을 사용할 수 없음. -> 무언가 아이디어만 떠오르면 쉽게 풀 수 있는 문제임. (공식)
# 아이디어를 떠올리는 것은 문제 풀이 경험으로 습득될 것 같음.

# 본 문제의 아이디어는 최적의 값과 현재의 값을 비교하는 것임. 주식 문제와 비슷한 아이디어.
# 현재의 값이 최적의 값보다 좋은 옵션이면, 최적의 값을 현재의 값으로 변경함.

import sys

n = int(sys.stdin.readline())
road_length = list(map(lambda x: int(x), sys.stdin.readline().split()))
gas_price = list(map(lambda x: int(x), sys.stdin.readline().split()))

result = 0
min_gas_price = sys.maxsize

for i in range(n-1):
    if gas_price[i] < min_gas_price:
        min_gas_price = gas_price[i]

    result += road_length[i] * min_gas_price

print(result)