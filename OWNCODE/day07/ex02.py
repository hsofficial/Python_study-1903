'''
ex02.py

제어문  Control Statement

코드의 흐름을 제어하는 구문
    -분기문 : 여러 지점으로 분기되는 코드
        if-else,if-elif(c언어에서 else if)-else
    -반복문 : 특정 구간 반복
        while, for
    -제어문 : 반복을 중단하거나 반복을 처음부터 다시 시작하거나 코드의 특정 위치로 곧바로 이동
        break, continue, pass
'''

value = 100

if value > 200:     #조건이 참인 경우에만 실행하고 조건이 거짓이면 실행하지 않는다
    print('크다')
    
if value % 2 == 1:  #value 값 홀수이면 홀수로 출력
    print('홀수')
    
if value % 2 == 0:  #value 값 짝수이면 짝수로 출력
    print('짝수')
    
if value % 2 == 1:  #value 값 홀수이면 홀수 출력 아니면 짝수라고 출력
    print('홀수')
else:
    print('짝수')
    
if value == 100:
    print('100')
if value % 2 == 0:
    print('짝수')
    
if value % 5 == 0:      #이 조건이 참이면 아니면에 해당하지 아니함
    print('5의 배수')
elif value % 2 == 0:    #아니면, value가 2의 배수인가
    print('2의 배수')
else:
    print('5와 2의 배수가 아님')