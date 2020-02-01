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

#연산자 대신 함수로 사칙연산
#1부터 10까지의 합을 구하는 코드 작성

total = 0
for i in range(1,11):
    total =     Add(total, i)
    
print(total)

#국영수 점수 입력받아 합계와 평균 출력

kr = int(input('Score of Korean : '))
en = int(input('Score of English : '))
ma = int(input('Score of Math : '))

scsum = Add(kr, en)
scsum = Add(scsum, ma)
scavg = Divide(scsum, 3)

print('합은 {}점, 평균은 {:.2f}점'.format(scsum, scavg))

#6자리 정수 전달받아 생년월일 형식으로 문자열 반환하는 함수 Birth()

def Birth(n):
    date = Remain(n, 100)
    n = int(Divide(n, 100))
    month = Remain(n, 100)
    year = int(Divide(n, 100))
    year = (year > 19) and Add(year, 1900) or Add(year, 2000)
    result ='{}년 {}월 {}일'.format(year, month,date)
    return result
    

word = Birth(930516)
print(word) #93년 5월 16일