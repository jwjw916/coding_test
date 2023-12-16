import sys
input = sys.stdin.readline
n = int(input())
stack = []

'''도저히 문제 이해가 안되서 찾아보니
1부터 오름차순으로 n개씩 주어지면
예제의 수열을 만들수 있냐 없냐였음
'''
# x = input()
# nums = [ x for x in range(1, n+1)]
# if not stack:
#     for num in nums:
#         stack.append(num)
#         if x == num:
#             break

# else:
#     if stack[-1] == x:
#         stack.pop()
#     else:

# 힌트: while로 쉽게 접근 가능함

start = 1
operator = []

for _ in range(n):
    end = int(input())
    while start <= end:
        stack.append(start)
        operator.append('+')
        start += 1
    
    if stack[-1] == end:
        stack.pop()
        operator.append('-')

    else: 
        print("NO")
        break

else:
    for i in operator:
        print(i)