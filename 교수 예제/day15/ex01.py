'''
ex01.py

파이썬 문제 풀이(함수)
'''

# 1. 반지름을 전달받아서 원의 넓이를 반환하는 함수 Circle()을 작성하세요
# (pi = 3.1415926535)
def Circle(r):
    pi = 3.1415926535
    return r * r * pi

print('{:.2f}'.format(Circle(3)))

# 2. 세 실수를 전달받아서 3개 변으로 구성된 삼각형이 직각삼각형인지 검증하여 True / False를 반환하는
# 함수 Pita() 를 작성하세요
def Pita(a, b, c):
    return a ** 2 + b ** 2 == c ** 2

print(Pita(3,4,5))
print(Pita(3,4,6))


# 3. 매개변수로 시간(분)을 전달받아서 타이머를 실행하고, 반환값이 없는 함수 Timer()를 작성하세요
from time import sleep
def Timer(minute):
    second = int(minute * 60)
    for i in range(second, -1, -1):
        print('\t{:02d} : {:02d}'.format(i // 60, i % 60))
        sleep(1)
    print('끝 !!')

Timer(0.06)

# 4. cm값을 입력받아서 inch값을 반환하는 함수 ReturnInch(cm)
# 1 inch = 2.54 cm
def ReturnInch(cm):
    return cm * 0.393701

print(ReturnInch(95), 'inch')

# 5. n GB = n * 1024 MB = n * 1024 * 1024 KB = n * 1024 * 1024 * 1024 Byte
# 용량을 숫자와 단위 모두 입력받아서 Byte로 반환하는 함수 toByte() 를 작성하세요   
def toByte(n):
    number = ''
    unit = ''
    for i in range(len(n)):
        if ord('0') <= ord(n[i]) and ord(n[i]) <= ord('9'): # isdigit()
            number += n[i]
        elif n[i] == '.':
            number += n[i]
        elif n[i] == ' ':
            pass
        else:
            unit += n[i]
            
    number = float(number)
            
    if unit.find('k') >= 0 or unit.find('K') >= 0: 
        return number * 1024
    elif unit.find('m') >= 0 or unit.find('M') >= 0: 
        return number * 1024 * 1024
    elif unit.find('g') >= 0 or unit.find('G') >= 0: 
        return number * 1024 * 1024 * 1024
    else:
        return None
    
print('{:,.2f}'.format(toByte('4.61222 m')))

# 4,836,998 (4,837,376)

# 6. Byte를 전달받아서 몇 KB/MB/GB인지 변환하는 함수 FileSize()를 작성하세요

def FileSize(n):

    cnt = 0
    unit = ''
    while n > 1024:     # 전달받은 값이 1024보다 크다면
        n = n / 1024    # 1024로 나누어서 값을 저장
        cnt += 1        # 나눌때 마다 cnt 를 1 증가
        
    if cnt == 1: unit = 'KB'
    elif cnt == 2: unit = 'MB'
    elif cnt == 3: unit = 'GB'
    return '{:,.2f} {}'.format(n, unit)
    
print(FileSize(4836998))

















