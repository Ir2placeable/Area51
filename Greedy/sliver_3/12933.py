# 12933 : 오리
# https://www.acmicpc.net/problem/12933
import sys
sound = sys.stdin.readline().rstrip()

sound_list = []
for item in sound:
    sound_list.append(item)
# print('sound list : ', sound_list)

ducks = 0
pattern = ['q', 'u', 'a', 'c', 'k']
while len(sound_list) > 0:
    item = sound_list[0]

    if item == 'q':
        i = 0
        pattern_index = 0
        while i < len(sound_list):
            if sound_list[i] == pattern[pattern_index]:
                sound_list.pop(i)
                pattern_index = (pattern_index+1) % 5
            else:
                i += 1
        if pattern_index != 0:
            ducks = -1
            break
        ducks += 1
    else:
        ducks = -1
        break
print(ducks)