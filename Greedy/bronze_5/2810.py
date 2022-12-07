# 2810 : 컵홀더
# https://www.acmicpc.net/problem/2810

people = int(input())
holders = people + 1

couple_seats = 0
for seat in input():
    if seat == 'L':
        couple_seats += 1

print(min(people, holders - couple_seats//2))
