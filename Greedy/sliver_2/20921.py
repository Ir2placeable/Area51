# 20921 : 그렇고 그런 사이
# https://www.acmicpc.net/problem/20921

n, k = map(lambda x: int(x), input().split(" "))
people = []
for i in range(0, n):
    people.append(i+1)

output = []
while n <= k:
    output.append(people.pop())
    k -= n - 1
    n -= 1

people.insert(n-k-1, people.pop())

def refine(input_list):
    result = ''
    for item in input_list:
        result += str(item) + ' '
    return result[:len(result)-1]

print(refine(output + people))
