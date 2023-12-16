'''
첫째줄 수만큼 반복
리스트 넣어서 정렬하고
순차출력
n 최대 백만
sort() = O(nlogn)
append() = O(1)
'''

import sys
input = sys.stdin.readline

n = int(input())
list = []
for _ in range(n):
    list.append(int(input()))
list.sort()
for x in list:
    print(x)

