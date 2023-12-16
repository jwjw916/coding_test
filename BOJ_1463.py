'''
x%3==0 then x = x//3
x%2==0 then x = x//2
or -1
문제: 1이 되는 연산의 최솟값
1 = 1
2 -> %2==0 -> x = x//2
3 -> %3==0 -> x = x//3
4 -> x != 1 -> %2==0 -> x//2
5 -> or -1 -> %2==0 -> x = x//2
6 -> %3==0 -> //3 -> 
x를 구성하는 이전 계산식 찾기 (점화식)

x = int(input())
ans = 0

if x == 1:
    print(x)
elif x == 2:
    print(x//2) -> 1번
elif x == 3:
    print(x//3) -> 1번
elif x%2!=0 or x%3!=0:
    x -= 1
    ans += 1 
    while x!=1:
        ans += 1
        if x%2==0:
            x = x//2
        elif x%3==0:
            x = x//3
    print(ans)
elif x%2 ==0 and x%3==0:
    x = x//3
    ans += 1
    while x!=1:
        ans += 1
        if x%2==0:
            x = x//2
        elif x%3==0:
            x = x//3
    print(ans)
'''

#시간초과로 문제접근을 아예 다르게함

n = int(input())
dp = [0]*(n+1) #연산 메모리 저장(연산횟수)
for i in range(2, n+1): 
    dp[i] = dp[i-1] + 1 #1은 1이기 때문에 빠지고, 2와 3으로 안나눠지면 -1 함

    if i%2==0:
        dp[i] = min(dp[i], dp[i//2]+1)

    if i%3==0:
        dp[i] = min(dp[i], dp(i//3)+1)
print(dp[n])