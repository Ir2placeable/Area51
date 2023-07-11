# https://www.acmicpc.net/problem/4673

nums = [i for i in range(10001)]
# print(nums)


def constructor(x):
    result = x
    for num in str(x):
        result += int(num)
    return result


index = 1
while index < 10001:
    temp = constructor(index)
    if temp < 10001:
        nums[temp] = 0

    if nums[index] != 0:
        print(index)

    index += 1