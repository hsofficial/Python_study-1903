'''
함수 반환값 이용하기
'''

def Add(n1, n2):
    return n1 + n2

def Minus(n1, n2):
    return n1 - n2

def Multi(n1, n2):
    return n1 * n2

def Divide(n1, n2):
    return n1 / n2

def Remain(n1, n2):
    return n1 % n2

# 이제부터 사칙연산에서는 연산자 대신 함수를 이용합니다

# 1. 1부터 10까지의 합을 구하는 코드를 작성하세요

total = 0
for i in range(1,11):
    total = Add(total, i)   # total += i    => total = total + i

print(total)

# 2. 국어, 영어, 수학 점수를 입력받아서 (변수값으로 초기화 해도 된다) 합계와 평균을 출력하세요
kor = 100
eng = 99
mat = 87

total = 0
avg = 0

total = Add(kor, eng)
total = Add(total, mat)

total = 0
total = Add(Add(kor, eng), mat)

avg = Divide(total, 3)
print('합계 : {}, 평균 : {:.2f}'.format(total, avg))


# 3. 6자리 정수를 전달받아 생년월일 형식으로 문자열로 반환하는 함수 Birth()를 작성
def Birth(num):
    date = Remain(num, 100)     # date = num % 100
    num = int(Divide(num, 100)) # num //= 100
    month = Remain(num, 100)    # month = num % 100
    year = int(Divide(num, 100))# year = num // 100
    #print(year, month, date)    값이 정상적으로 구해졌는지 확인하기
    year = (year > 19) and Add(year, 1900) or Add(year, 2000)
    str1 = '{}년 {}월 {}일'.format(year, month, date)
    return str1

word = Birth(930516)
print(word)

























