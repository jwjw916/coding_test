import sys
input = sys.stdin.readline

n = int(input())
list_ = set(input().rstrip() for _ in range(n))

list = sorted(list_) #사전순

list = sorted(list, key=len) #길이순

for i in list:
    print(i)

# 파이썬 정렬 - 우선순위 낮은순으로 정렬