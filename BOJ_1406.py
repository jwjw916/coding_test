import sys
input = sys.stdin.readline

# word = list(map(str,input()))
# n = int(input())
# cursor = n+1

# for _ in range(n):
#     x = str(input())
#     if x == 'L' and cursor != 0:
#         cursor -= 1
#     elif x == 'D' and cursor != n+1:
#         cursor += 1
#     elif x == 'B' and cursor != 0:
#         y = cursor 
#         word.pop(y)
#     elif "P" in x:
#         z = x.split()
#         y = cursor  if cursor != 0 else 0
#         word.insert(y, z[1])

# print(''.join(word))

st1 = list(input().rstrip())
st2 = []

for _ in range(int(input())):
    command = list(input().split())
    if command[0] == "L":
        if st1:
            st2.append(st1.pop())
    elif command[0] == "D":
        if st2:
            st1.append(st2.pop())
    elif command[0] == "B":
        if st1:
            st1.pop()
    else:
        st1.append(command[1])
st1.extend(reversed(st2))
#reversed(st2) 는 st2에 값이 존재하지 않더라도 
#오류를 띄우지 않고 우리가 생각한대로 잘 작동한다.
print(''.join(st1))

'''
시간복잡도 
https://seongonion.tistory.com/53
이렇게 생각하는 습관들이기'''