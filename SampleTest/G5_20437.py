# https://www.acmicpc.net/problem/20437

# 시간복잡도에 대한 고민을 해야한다.
# 메모리 제한 크기가 매우크다 -> 메모리를 이용하는 방법을 사용해야 한다.
# 윈도우를 만드는 방식을 고민해야 한다.

import sys
from collections import defaultdict

test_case = int(sys.stdin.readline())
for _ in range(test_case):
    string = list(sys.stdin.readline().rstrip())
    k = int(sys.stdin.readline())

    candidates = set()
    for char in string:
        if string.count(char) >= k:
            candidates.add(char)

    result1 = 10001
    result2 = 0
    for item in candidates:
        start = string.index(item)
        count = 1
        for i in range(start + 1, len(string)):
            if string[i] == item:
                count += 1
            if count == k:
                result1 = min(result1, i - start + 1)

                if string[i] == string[start]:
                    result2 = i - start + 1
                break

    if result2 == 0:
        print(-1)
        continue
    print(result1, result2)
