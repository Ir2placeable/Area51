# 2872 : 우리집엔 도서관이 있어
# https://www.acmicpc.net/problem/2872

n = int(input())
books = []
for i in range(0, n):
    books.append(int(input()))

continuous = 0
target = 0
for i in range(0, n):
    if target < books[i]:
        continuous += 1
        target = books[i]
print(n - continuous)
