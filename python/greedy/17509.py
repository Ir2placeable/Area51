# 17509 : And the Winner Is... Ourselves!
# https://www.acmicpc.net/problem/17509

# 11줄 고정
# 각 줄에 D, V
# What is the minimum penalty if we solve all problems?

# T + 20V

times = 0
sum_times = 0
questions = []
for i in range(0, 11):
    a, b = map(lambda x: int(x), input().split(" "))
    questions.append([a, b])

questions.sort()

for question in questions:
    times += question[0]
    sum_times += times + 20 * question[1]

print(sum_times)