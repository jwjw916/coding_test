import sys
input = sys.stdin.readline()

n = int(input())

for _ in range(n):
    words = input().split()
    for i in words:
        print(i[::-1] , end=" ")

# 스택을 이용한 풀이
for i in range(n):
    string = input()
    string+=" "
    stack = []
    for j in string:
        if j!=" ":
            stack.append(j)
        else:
            while stack:
                print(stack.pop(), end='')
            print(' ', end='')