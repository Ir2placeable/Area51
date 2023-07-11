# https://www.acmicpc.net/problem/20437

# 알파벳 소문자로 이루어진 문자열 W가 주어진다.
# 양의 정수 K가 주어진다.
# 어떤 문자를 정확히 K개를 포함하는 가장 짧은 연속 문자열의 길이를 구한다.
# 어떤 문자를 정확히 K개를 포함하고, 문자열의 첫 번째와 마지막 글자가 해당 문자로 같은 가장 긴 연속 문자열의 길이를 구한다.
# (1 ≤ K ≤ |W| ≤ 10,000)

import sys
from collections import defaultdict

test_case = int(sys.stdin.readline())
for _ in range(test_case):
    stringW = sys.stdin.readline().rstrip()
    target = int(sys.stdin.readline())
    result1, result2 = sys.maxsize, 0

    alphabet_locations = defaultdict(list)
    for i in range(len(stringW)):
        char = stringW[i]
        alphabet_locations[char].append(i)

    isResult = False
    for alphabet in alphabet_locations:
        if len(alphabet_locations[alphabet]) < target:
            continue
        isResult = True

        alphabet_indexes = alphabet_locations[alphabet]
        for index in range(len(alphabet_indexes)):
            if index + target - 1 < len(alphabet_indexes):
                result1 = min(result1, alphabet_indexes[index + target - 1] - alphabet_indexes[index] + 1)
                result2 = max(result2, alphabet_indexes[index + target - 1] - alphabet_indexes[index] + 1)

    if isResult:
        print(result1, result2)
    else:
        print(-1)