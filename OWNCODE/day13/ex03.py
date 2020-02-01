'''
ex03.py

함수 만들기 문제
'''
#1. 정수를 전달받아서 전달받은 정수의 자릿수를 뒤집은 수를 반환하는 함수 Reverse()

def Reverse(num):    
    result = 0
    while num > 10:
        result += num % 10
        result *= 10
        num //= 10
    result += num
    return result   #함수의 반환값은 함수의 호출 영역 전체를 대체함
    
print(Reverse(1234))


#2. 정수를 두개 전달 받아서 두 수 사이의 정수를 한줄로 출력하는 함수 Range()

def Range(n1, n2):
    i = n1
    while i <= n2:
        print(i,' ', end = '')
        i += 1
        
Range(1, 9)

print()

def Range2(n1, n2):
    for i in range(n1, n2 + 1, 1):
        print(i,' ', end = '')       
    print()
    
Range2(1, 10)


#3. 세 정수를 전달받아서 절대값 가장 큰 수를 반환하는 함수 MaxAbs()

def MaxAbs(n1, n2, n3):
    an1 = abs(n1)
    an2 = abs(n2)
    an3 = abs(n3)
    
    #an1 = n1 < 0 and -n1 or n1   >>>절대값 중에서 가장 큰 수 구한 후에
    #an2 = n2 < 0 and -n2 or n2
    #an3 = n3 < 0 and -n3 or n3    
    #max = an1                    >>>절대값이 가장 큰 원래의 수 반환
    #max = max < an2 and an2 or max
    #max = max < an3 and an3 or max     
        
    result = n1
    if an2 > an1:        result = n2
    if an3 > an1:        result = n3
    
    return result

print( MaxAbs(-5, 21, -30) )


#4. 정수를 하나 전달받아서 전달받은 정수까지의 소수를 출력하는 함수 PrimeNumber()

def PrimeNumber(n):
    for i in range (2, n + 1 ):      # 범위 지정 >>> 범위중 특정 숫자가 i
        chk = True                 # 소수 판별 check 논리연산 >>> false 인지 아닌지 검사
        for x in range(2, i + 1):   # x 값이 1부터 1씩 증가하면서 i-1이 될때까지 반복
            if i != x and i % x == 0:          # i를 x로 나눈 나머지가 0
                chk = False         # chk에 False을 저장(자기자신을 제외하고 나누어 떨어지면 조건 탈락)
                break                   # 반복문 종료
        if chk == True:             # chk 값이 False가 아니면 소수이므로 출력
            print(i, end=" ")

PrimeNumber(30)

    