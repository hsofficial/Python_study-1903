'''
ex01.py

기본 if 문제
'''

#세 수를 입력받아 최대값 출력

num1 = int(input('정수 입력 : '))
num2 = int(input('정수 입력 : '))
num3 = int(input('정수 입력 : '))

if num1 < num2:    ans1 = num1
else:    ans1 = num2

if ans1 > num3:    ans1 = num3

print(ans1)
print()

#세 수를 입력받아 최소값 출력
num4 = int(input('정수 입력 : '))
num5 = int(input('정수 입력 : '))
num6 = int(input('정수 입력 : '))

if num4 > num5:    ans2 = num4
else:    ans2 = num5

if ans2 < num6:    ans2 = num6

print(ans2)
print()

#입력 받은 수의 절대값 출력
num7 = int(input('정수 입력 : '))

if num7 < 0:    num7 = -num7

print(num7)
print()