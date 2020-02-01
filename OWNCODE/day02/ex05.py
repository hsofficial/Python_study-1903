'''
자료형

data
입력 - 처리 - 출력

data type : 자료형, 자료의 형태
'''

var1=10
var2=3.14
var3='아이유'

print(var1, var2, var3)

'''자료형을 확인하는 기능 type()'''
print('type(var1) : ', type(var1))
print('type(var2) : ', type(var2))
print('type(var3) : ', type(var3))

'''
num1 = input("숫자 입력 :")
num2 = input("숫자 입력 :")

num1 = int(num1)
num2 = int(num2)
'''

num1=int(input("숫자 입력 :"))
num2=int(input("숫자 입력 :"))
print(num1, "+", num2, "=", num1 + num2)
print()

num3=float(input('키 입력(cm) :'))
num3=num3 + 10
print('키:', num3, 'cm')

'''산술 연산(사칙연산)'''
print('산술연산자')
n1 = 10
n2 = 3
print(n1 + n2)
print(n1 - n2)
print(n1 * n2)
print(n1 / n2)
print(n1 // n2)    #정수 몫만 나눗셈
print(n1 % n2)
print(n1 ** n2)    #제곱(승수)