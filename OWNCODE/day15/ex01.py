'''
 ex01.py
 파이썬 문제 풀이(함수)
'''
#반지름을 전달받아서 원의 넓이를 변환하는 함수 Circle()

def Circle(r):
    pi = 3.14
    result = r * r * pi
    return result

print('원의 넓이는', Circle(3), 'cm^2')

#세 실수를 전달받아서 3개 변으로 구성된 삼각형이 직각삼각형인지 검증하여 TF 반환 함수 Pita()
#a^2+b^2=c^2

def Pita(a, b, c):
    result_2 = 0
    maxval = a
    second = b
    third = c
    
    if b > maxval:
        maxval = b
        second = c
        third = a
        
    if c > maxval:
        maxval = c
        second = b
        third = a
            
    if maxval * maxval == (second * second) + (third * third):
        result_2 = True
        
    else:
        result_2 = False
        
    return result_2

print('Is it Right triangle? : ', Pita(3, 4, 5))

#매개변수로 분 전달받아 타이머 실행 반환값 없는 함수 Timer

from time import sleep
from os import system

def Timer(m):    
    second = m * 60
    
    for i in range(second, -1, -1):
        system("cls")
        print('{:02d} min : {:02d} sec'.format(i // 60, i % 60))
        sleep(1)
        
    print('end')

Timer(0)

#cm 입력 inch 반환 ReturnInch(cm)

def ReturnInch(cm):
    inch = cm * 2.54
    return inch

print(ReturnInch(10), 'inch')

#용량 byte 변환 toByte()    >>> 단위+수 입력, 1024byte=1M

def toByte(size):
    size = str(size)
    met = size[-2:]
    fx = size[:-2]
    fx = float(fx)
    byte = 0

    if met == 'TB':
        byte = fx * (2 ** 40)
    
    elif met == 'GB':
        byte = fx * (2 ** 30)
    
    elif met == 'MB':
        byte = fx * (2 ** 20)
    
    elif met == 'KB':
        byte = fx * (2 ** 10)
    
    else:
        byte = fx
    return byte

print(toByte('10 TB'), 'Byte' )

#byte >> KB MB GB 변환 FileSize()

def FileSize(byte):
    
    cnt = 0
    unit = ''
    while byte > 1024:     # 전달받은 값이 1024보다 크다면
        byte = byte / 1024    # 1024로 나누어서 값을 저장
        cnt += 1        # 나눌때 마다 cnt 를 1 증가
        
    if cnt == 1: unit = 'KB'
    elif cnt == 2: unit = 'MB'
    elif cnt == 3: unit = 'GB'
    elif cnt == 4: unit = 'TB'
    return '{:,.2f} {}'.format(byte, unit)

'''
    KB = byte // 1024
    MB = KB // 1024
    GB = MB // 1024
    TB = GB // 1024
    sizeres = '{:,.2f} Byte is {:,.2f} KB, {:,.2f} MB, {:,.2f} GB and {:,.2f} TB.'.format(byte,KB,MB,GB,TB)
    return sizeres
'''

print(FileSize(10995116277760))

