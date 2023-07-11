# 23028 : 5학년은 다니기 싫어요
# https://www.acmicpc.net/problem/23028

# 졸업학점 : 130 / 전공필수 : 66
# semester : 현재 학기 / now_major : 현재 전공학점 / now_all : 현재 총 학점
# major : 개설 전공과목 수 / non_major : 개설 비전공과목 수 / 과목당 3학점
# 한 학기 당 최대 6개 수강 가능
# 8학기 안에 졸업이 가능하면 Nice or Nae ga wae 출력

semester, now_major, now_all = map(lambda x: int(x), input().split(" "))
need_major = 66 - now_major
need_all = 130 - now_all

condition1 = False
for i in range(0, 10):
    major, non_major = map(lambda x: int(x), input().split(" "))

    if need_major <= 0 and need_all <= 0:
        condition1 = True
        continue
    elif semester > 8:
        continue

    need_major -= major * 3
    need_all -= major * 3
    need_all -= min(6 - major, non_major) * 3
    semester += 1

# print(condition1, semester)

if condition1 == True and semester <= 8:
    print('Nice')
else:
    print('Nae ga wae')
