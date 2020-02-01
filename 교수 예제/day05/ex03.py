'''
ex03.py

문자열.format() 함수 사용 법
'''

name = '이승기'
age = 33

result = '{:s}님의 나이는 {:d}살입니다'.format(name, age)
print(result)
print()

num = 11
print('num(10) : {:d}'.format(num))     # 10진수
print('num(16) : {:x}'.format(num))     # 16진수(소문자)
print('num(16) : {:02x}'.format(num))   # 16진수(공백은0으로)
print('num(16) : {:02X}'.format(num))   # 16진수(대문자)
print('num(08) : {:o}'.format(num))     # 8진수
print('num(02) : {:b}'.format(num))     # 2진수

# 진법 변환 예제
ip = input('IP주소를 입력 : ')       # 192.168.201.100
n1, n2, n3, n4 = ip.split('.')    # 문자열 
# split() : ()안에 들어가는 문자를 구분자로 지정하여 각 필드를 구분한다

n1 = int(n1)        # 정수 변환
n2 = int(n2)        # 자료형 변환
n3 = int(n3)        # 문자열 형태를 정수로 변환하여 원래 자리에 새로 대입
n4 = int(n4)

print('{:08b}'.format(n1), end='.')
print('{:08b}'.format(n2), end='.')
print('{:08b}'.format(n3), end='.')
print('{:08b}'.format(n4))

print('{:02X} {:02X} {:02X} {:02X}'.format(n1, n2, n3, n4))

























