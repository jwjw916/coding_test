'''
3 or 5kg 봉지를 최소한으로 가져가기
5로 나눠지면 -> 전부 5kg
3씩 담다가 -> 5로 나눠지면 5kg
안되면 -1 출력

while 사용
'''

import sys
input = sys.stdin.readline

n = int(input())
bag = 0
while n >= 0:
    if n % 5 == 0:
        bag += n // 5
        print(bag)
        break
    n -= 3
    bag += 1

else:
    print(-1)
