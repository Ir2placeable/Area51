# https://www.acmicpc.net/problem/20922

# 같은 것이 k개 이하인 사실을 판별하기 위해서는 dict을 사용해야 한다 -> defaultdict 사용하기
# 부분수열의 길이는 defaultdict의 values 를 sum한 값이다.
# sum(dict.values()) 하는 경우 -> 시간 초과 발생한다.
# 따라서, dict의 values 개수를 변수로 따로 관리한다. -> count

import sys
from collections import defaultdict

n, k = map(lambda x: int(x), sys.stdin.readline().split())
numbers = list(map(lambda x: int(x), sys.stdin.readline().split()))

left, right = 0, 0
window = defaultdict(int)
count = 0
result = 0

while left <= right < n:
    if window[numbers[right]] >= k:
        window[numbers[left]] -= 1
        if window[numbers[left]] == 0:
            del window[numbers[left]]
        left += 1
        count -= 1
    else:
        window[numbers[right]] += 1
        right += 1
        count += 1

    result = max(result, count)
print(result)