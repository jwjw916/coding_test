import sys
input = sys.stdin.readline




def chk(n):
    stack = []
    for y in x:
        if y == "(":
            stack.append(y)
        else:
            if stack:
                stack.pop()
            else:
                return "NO"
                
    if stack:
        return "NO"
    else:
        return "YES"

        
n = int(input())
for _ in range(n):
    x = input()
    print(chk(x))

        
