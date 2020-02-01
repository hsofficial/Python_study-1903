'''
ex02.py

함수의 구조
'''
#def 함수를 정의 / 이름과 내용
def add (n1, n2):
    result = n1 + n2
    return result
    #return 기능 >>> 함수의 종료 또는 값의 반환

print('{}+{}={}'.format(1,2,add(1,2) ) )
#함수의 이름을 부르면서 입력값 전달 // 함수의 호출 (Call)

print('{}+{}={}'.format(64,128,add(64,128) ) )

#ex1.두 수를 전달받아 두 수 가운데 큰 수를 반환하는 함수 Big()

def Big(n1, n2):
    big = 0
    if n1 > n2:        big = n1
    else:        big = n2
    return big

print('{}과 {} 가운데 큰 수는 = {}'.format(3,100,Big(3,100) ) )

#Q1.세 수를 전달받아 세 수 가운데 큰 수를 반환하는 함수 Test1()

def Test1(n1, n2, n3):
    result = n1
    if n2 > result:        result = n2
    if n3 > result:        result = n3
    return result

n1 = 3
n2 = -5
n3 = 4
maximum = Test1(n1, n2, n3)
print('{}, {}, {}중 가장 큰 수는 {}'.format(n1, n2, n3, maximum) )

#Q2.정수 6자리를 전달받아서 년월일 구성 문자열 반환 함수 Birth()

def Birth(n):
    date = n % 100
    n = n // 100
    month = n % 100
    year = n // 100
    result ='{}년 {}월 {}일'.format(year, month,date)
    return result
    

word = Birth(930516)
print(word) #93년 5월 16일

#ex2.정수를 전달받아서 정수가 홀수인지 짝수인지 판별하는 함수 isEven()

def isEven(num):
    if num % 2 == 0:
        return True
    else:
        return False
n1 = 3
print('n1 is even number? :', isEven(n1) )

#Q3.정수 하나를 전달받아서 정수가 3의 배수인지 판별하는 함수 Test2()

def Test2(num):
    if num % 3 == 0:
        return True
    else:
        return False
n2 = 7
print('n2 is 3x number? :',Test2(n2))
