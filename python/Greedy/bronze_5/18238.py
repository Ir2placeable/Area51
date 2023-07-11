# 18238 : ZOAC2
# https://www.acmicpc.net/problem/18238

string = input()

times = 0
index = 'A'
for char in string:
    require_moves = max(ord(index)-ord(char), ord(char)-ord(index))

    if require_moves > 13:
        require_moves = 26 - require_moves

    index = char
    times += require_moves

print(times)
