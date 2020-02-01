'''
ex02.py

제어문 : Control Statement

코드의 흐름을 제어하는 구문
    - 분기문 : 여러 지점으로 분기되는 코드를 만든다
        if, if ~ elif ~ else
    - 반복문 : 특정 구간을 반복하도록 만든다
        while, for
    - 제어문 : 반복을 중단하거나, 반복을 처음부터 다시 시작하거나, 코드의 특정 위치로 곧바로 이동
        break, continue, pass
'''

val = 100

if val > 200:       # 조건이 참인 경우에만 실행하고, 조건이 거짓이면 실행하지 않는다
    print('크다')
    

if val % 2 == 1:    # val의 값이 홀수이면 홀수라고 출력하자
    print('홀수')
if val % 2 == 0:
    print('짝수')    # val의 값이 짝수이면 짝수라고 출력하자
    
    
if val % 2 == 1:    # 만약, val의 값이 홀수이면 홀수2라고 출력하고
    print('홀수2')
else:               # 아니면, 짝수2라고 출력하자 (조건을 따로 갖지 않고, 이전 if의 반대 조건을 사용한다)
    print('짝수2')



if val == 100:
    print('100')
if val % 2 == 0:
    print('짝수')
    

if val == 100:
    print('100')
else:
    print('짝수')
    

val = 102
if val % 5 == 0:        # 이 조건이 참이면, '아니면'에 해당하지 않는다
    print('5의 배수')

elif val % 2 == 0:      # 아니면, val이 2의 배수인가
    print('2의 배수')
    
else:
    print('5의 배수도 아니고, 2의 배수도 아니다')    









