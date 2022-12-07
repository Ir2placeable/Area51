# 12788 : 제 2회 IUPC는 잘 개최될 수 있을까?
# https://www.acmicpc.net/problem/12788

club_members = int(input())

teams, team_members = map(lambda x: int(x), input().split(" "))
need_pens = teams * team_members

pen_list = list(map(lambda x: int(x), input().split(" ")))
pen_list.sort(reverse=True)

index = 0
pens = 0
flag = False
while 1:
    pens += pen_list[index]
    index += 1

    if pens >= need_pens:
        flag = True
        break
    if index == club_members:
        break
if flag:
    print(index)
else:
    print('STRESS')