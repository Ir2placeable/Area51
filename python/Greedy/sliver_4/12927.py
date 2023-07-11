# 12927 : 배수 스위치
# https://www.acmicpc.net/problem/12927

input_str = input()
bulbs = []
for bulb in input_str:
    bulbs.append(bulb)

need_switches = 0
for i in range(0, len(bulbs)):
    if bulbs[i] == 'Y':
        temp_index = i
        while temp_index < len(bulbs):
            bulbs[temp_index] = 'N' if bulbs[temp_index] == 'Y' else 'Y'
            temp_index += i+1
        need_switches += 1

print(need_switches)