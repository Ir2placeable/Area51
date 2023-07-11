# 16162 : 가희와 3단 고음
# https://www.acmicpc.net/problem/16162

n, start_pitch, add_pitch = map(lambda x: int(x), input().split(" "))
pitches = list(map(lambda x: int(x), input().split(" ")))

max_note = 0
target_pitch = start_pitch
for pitch in pitches:
    if pitch == target_pitch:
        max_note += 1
        target_pitch += add_pitch

print(max_note)