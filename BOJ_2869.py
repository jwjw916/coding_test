'''
높이 v
낮에 +A
밤에 -B
'''

list = list(map(int, input().split()))
A = list[0]
B = list[1]
V = list[2]
C = 0
#5미터, 
#2미터 올라가고 
#1미터 미끄러지면..
#하루에 1미터 올라가네
#근데 마지막날에는 올라가면 안미끄러지니까
#  1,2,3, 3+2 >=5미터니까
#  4일째 성공
D = 1
while V>=C:
    C = D * (A-B)
    D += 1
    if A+C >= D:
        break
print(D+1)
    
