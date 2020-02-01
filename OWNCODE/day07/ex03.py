'''
ex03.py
'''

#1. 사용자에게 정수를 입력받아서 2의 배수인지 3의 배수인지 2와 3의 공배수인지 판별하는 코드 if로 작성
#if elif else 자유롭게 사용

num = int(input('정수 입력 :'))

'''
if num % 2 == 0:
    print('2의 배수')
else:
    print('2의 배수가 아님')

if num % 3 == 0:
    print('3의 배수')
else:
    print('3의 배수가 아님')
'''
    
if num % 2 == 0 and num % 3 == 0 :  #조건 중 가장 먼저 처리해야할 것을 맨 위에 둔다
    print('2와 3의 공배수')
elif num % 2 == 0:
    print('2의 배수')
elif num % 3 == 0:
    print('3의 배수')
else:                               #이전의 if elif가 처리하지 못한 모든 경우를 else가 처리함
    print('2와 3의 배수가 아님')