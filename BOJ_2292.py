'''
육각형.. 길이 여섯갈래인데
1-> 아래로 +6
7 -> 아래로 +12   -3 = 4 
19-> 아래로 +18   -6 = 13 
37 +24   -9 = 28 
61 +30   -12 = 49
6의 배수만큼가니깐
반대편끼리는 3의 배수만큼 차이가 난다

아, 몇개의 방을 지나가는지 = 6배수 몇칸을 지나는지
'''

import sys
input = sys.stdin.readline

n = int(input())
path = 1 #시작하는 칸 포함
cnt = 1 #지나가는 칸 개수

while n > path:
    path += 6 * cnt
    cnt += 1
print(cnt)