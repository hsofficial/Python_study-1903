'''
ex03.py
'''

# 1. 사용자에게 정수를 입력받아서, 2의 배수인지, 3의 배수인지, 2와 3의 공배수인지, 해당없는지 판별하는 코드를 
# if 를 이용하여 작성하세요 (elif, else도 자유롭게 사용하세요)

'''
if는 조건을 제시한다
elif는 if의 조건이 아닌 경우 또다른 조건을 제시한다
else는 이전의 if나 elif가 제시하는 조건이 모두 거짓인 경우를 처리한다

if A:
    print('A')
elif B:
    print('B')
elif C:
    print('C')
else:
    print('D')
'''

data = int(input('정수 입력 : '))

if (data % 2 == 0 and data % 3 == 0):   # 조건중 가장 먼저 체크해야할 조건을 맨 위에 올려둔다
    print('2와 3의 공배수')
elif (data % 2 == 0):
    print('2의 배수')
elif (data % 3 == 0):   # else if
    print('3의 배수')
#elif (not(data % 2 == 0) and not(data % 3 == 0)):
else:           # 이전의 if나 elif가 처리하지 못한 모든 경우를 else가 처리한다
    print('2나 3의 배수가 아님')
    
    



