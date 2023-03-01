# https://www.acmicpc.net/problem/1515
import sys


def getCases(cur, index):
    if cur:
        cases.append(''.join(cur))

    for i in range(index, n):
        getCases(cur + [nums[i]], i + 1)


target_string = sys.stdin.readline().rstrip()

result_string = ''
target_number = 1
result = 0

while len(result_string) < len(target_string):
    # 붙일 수 있는 문자열을 모두 구한다.
    nums = list(str(target_number))
    n = len(nums)

    cases = []
    getCases([], 0)
    cases.sort(reverse=True)

    # 붙일 수 있는 경우의 수를 모두 비교한다.
    for case in cases:
        temp_string = result_string + case
        if temp_string == target_string[:len(temp_string)]:
            result_string = temp_string
            break

    result = target_number
    target_number += 1

print(result)