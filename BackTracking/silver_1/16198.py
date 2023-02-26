# https://www.acmicpc.net/problem/16198
import sys
from copy import deepcopy


def backTracking(cur_energy, left_list):
    global result

    if len(left_list) == 2:
        result = max(result, cur_energy)
        return

    for i in range(1, len(left_list) - 1):
        left_list_copy = deepcopy(left_list)
        cur_energy_copy = cur_energy

        cur_energy_copy += left_list_copy[i-1] * left_list_copy[i+1]
        left_list_copy.pop(i)
        backTracking(cur_energy_copy, left_list_copy)


n = int(sys.stdin.readline())
nums = list(map(lambda x: int(x), sys.stdin.readline().split()))

result = 0
backTracking(0, nums)
print(result)