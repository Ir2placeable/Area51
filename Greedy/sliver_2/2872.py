# 2872 : 우리집엔 도서관이 있어
# https://www.acmicpc.net/problem/2872

# 최대 수인 n 부터 하나씩 줄여가며 위로 올려야 한다.
#

n = int(input())
books = []
for i in range(0, n):
    books.append(int(input()))

now = 0
moves = 0
for i in range(0, n):
    if books[i] == n:
        moves += n-i-1
        break
    if books[i]+1 != books[i+1]:
        moves += 1

print(moves)