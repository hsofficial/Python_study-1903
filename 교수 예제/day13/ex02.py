'''
ex02.py

함수의 구조
'''
from test.test_itertools import isEven

# def : 함수를 정의(definition) Add라는 이름을 가진 함수가 있고, 내용은 이렇다
def Add(n1, n2):
    result = n1 + n2
    return result   # return 의 기능 1. 함수의 종료 | 2. 값의 반환 

print('{} + {} = {}'.format(1, 2, Add(1, 2)))
#                                함수의 이름을 부르면서 입력값을 전달
#                                함수의 호출(Call)


print('{} + {} = {}'.format(64, 128, Add(64, 128)))
print()

# 예제 1. 두 수를 전달받아서, 두 수중 큰 수를 반환하는 함수 Big()을 작성해보자

def Big(n1, n2):
    big = 0
    if n1 > n2: big = n1
    else:       big = n2
    return big

print('{}와 {}중 큰 수는 {}이다\n'.format(3,100, Big(3, 100)))

# 문제 1. 세 수를 전달받아서 세 수중 가장 큰 수를 반환하는 함수 Test1()을 작성해보자

def Test1(n1, n2, n3):
    max = n1
    if max < n2: max = n2
    if max < n3: max = n3
    return max

n1 = -30
n2 = -5
n3 = -50
max = Test1(n1, n2, n3)
print('{}, {}, {} 중 가장 큰 수는 {}이다'.format(n1, n2, n3, max))


# 문제 2. 정수 6자리를 전달받아서, 연, 월, 일로 구성된 문자열을 반환하는 함수 Birth()를 작성하세요

def Birth(n):
    date = n % 100  # 16
    n = n // 100    # 9305
    month = n % 100 # 05
    year = n // 100 # 93
    result = '{}년 {}월 {}일'.format(year, month, date)
    return result

# data = int(input('생년월일 6자리를 입력 : '))
word = Birth(930516)
print(word) # 93년 5월 16일


# 예제 2. 정수 하나를 전달받아서, 정수가 홀수인지 짝수인지 판별하는 함수 isEven()

def isEven(num):
    if num % 2 == 0:
        return True
    else:
        return False

n1 = 4
print('n1이 짝수인가 :', isEven(n1))

# 문제 3. 정수 하나를 전달받아서, 정수가 3의 배수인지 판별하는 함수 Test2()를 작성하세요

def Test2(num):
    pass

n2 = 7
print('n2가 3의 배수인가 :', Test2(n2))
































