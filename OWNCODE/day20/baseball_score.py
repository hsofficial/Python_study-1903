'''
baseball_score.py
'''

from random import randint
from os import system

n1, n2, n3 = 0, 0, 0


while True:
    n1 = randint(1, 9)      # 0 에서 9 사이의 랜덤한 수를 만든다(실행할 때마다 값이 바뀐다)
    n2 = randint(0, 9)
    n3 = randint(0, 9)
    flag = n1 != n2 and n1 != n3 and n2 != n3
    if flag:
        break

# 정답을 미리 보여주는 코드    
#print(n1, n2, n3)

cnt = 0
while True:
    strike, ball ,out = 0,0,0
    user = input('숫자 입력 : ')
    if user.isdigit():      #숫자로만 구성
        user = int(user)    #정수형으로 변환
        u3 = user % 10      #자릿수 구분
        user //= 10
        u2 = user % 10
        u1 = user // 10
        cnt += 1
        
        #스트라이크 판별
        if n1 == u1: strike += 1
        if n2 == u2: strike += 1
        if n3 == u3: strike += 1
        
        #볼 판별
        if n1 == u2 or n1 == u3: ball += 1
        if n2 == u1 or n2 == u3: ball += 1
        if n3 == u1 or n3 == u2: ball += 1
        
        #아웃 판별
        out = 3 - strike - ball
        
        print('\n\t{} Strike, {} Ball, {} Out \n'.format(strike, ball, out))
        if strike == 3:
            print('정답 : [{} {} {}]'.format(n1, n2, n3))
            print('축하합니다. {}회만에 성공하셨습니다'.format(cnt))
            system('pause')
            break
    elif user == 'exit' or user == 'quit' or user == 'gg':
        print('\n\t다음에 또 봐요\n')
        break
         
    else:
        print('\n\t수를 다시 입력하세요\n')