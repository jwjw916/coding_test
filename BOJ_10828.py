import sys
input = sys.stdin.readline

n = int(input())
stack = []

for i in range(n):
    x = input().split()
    if "push" == x[0]:
        v = x[1]
        stack.append(v)
    elif "top" == x[0]:
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
    elif "size" ==x[0]:
        print(len(stack))
    elif "pop" == x[0]:
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif "empty" == x[0]:
        if len(stack) == 0:
            print(1)
        else:
            print(0)

