# 6550 : 부분 문자열
# https://www.acmicpc.net/problem/6550

while True:
    try:
        sub_string, super_string = input().split(" ")
        sub_string_index = 0

        result = False
        for char in super_string:
            if char == sub_string[sub_string_index]:
                sub_string_index += 1
            if sub_string_index == len(sub_string):
                result = True
                break

        if result:
            print('Yes')
        else:
            print('No')
    except:
        exit(0)