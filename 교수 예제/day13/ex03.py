'''
ex03.py

함수 만들기 문제
'''

# 1. 정수를 전달받아서 전달받은 정수의 자릿수를 뒤집은 수를 [반환]하는 함수 Reverse()를 작성
def Reverse(num):
    ret = 0
    while num > 10:
        ret += num % 10
        ret *= 10
        num //= 10
    ret += num
    return ret      # 함수의 반환값은 함수의 호출 영역 전체를 대체한다
    
print(Reverse(1234))    # 4321
# print(4321)

# 2. 정수를 두 개 전달받아서 두 수 사이의 정수를 한줄로 [출력]하는 함수 Range()를 작성
def Range(n1, n2):
    i = n1                      # 초기값     1
    while i != n2 + 1:          # 반복 조건 2
        print(i, '', end='')    # 실행문     3
        i += 1                  # 증감식     4
    print()
    #              1     2     4
    for i in range(n1, n2 + 1, 1):
        print(i, '', end='')    # 3
    print()

Range(1,10)     # 1 2 3 4 5 6 7 8 9 10


# 3. 세 정수를 전달받아서, 절대값이 가장 큰 수를 [반환]하는 함수 MaxAbs()를 작성
def MaxAbs(n1, n2, n3):
    ab1 = n1 < 0 and -n1 or n1      # 절대값을 먼저 구하고
    ab2 = n2 < 0 and -n2 or n2
    ab3 = n3 < 0 and -n3 or n3
    
    max = ab1                       # 절대값 중에서 가장 큰 값을 구한 후에
    max = max < ab2 and ab2 or max
    max = max < ab3 and ab3 or max
    
    if max == ab1: return n1        # 절대값이 가장 큰 원래의 수를 반환한다
    if max == ab2: return n2
    if max == ab3: return n3
    

print(MaxAbs(10, -20 , 15))    # -20

# 4. 정수를 하나 전달받아서, 전달받은 정수 까지의 소수를 [출력]하는 함수 PrimeNumber()를 작성
def PrimeNumber(num):
    for i in range(2, num + 1):     # 전체 범위 중에서
        flag = True                 # 조건이 참인지 거짓인지 저장할 변수(flag의 값에 따라서 결과가 달라진다)
        for j in range(2, i + 1):   # i가 소수인지 판단하여
            if i != j and i % j == 0:   # 소수가 아니면 flag = False
                flag = False
                break
        if flag:                    # flag가 True이면 i를 출력
            print(i, end=' ')
            

#PrimeNumber(20) # 2, 3, 5, 7, 11, 13, 17, 19
print()














