'''
ex02.py

Operator(연산자) : 수식에서 각종 계산을 처리하는 기호나 글자들의 모임

'''

n1 = 10
n2 = 3

# 1. 산술연산
print(n1 + n2)
print(n1 - n2)
print(n1 * n2)
print(n1 / n2)
print(n1 // n2)    #정수 몫만 나눗셈
print(n1 % n2)    #나머지
print(n1 ** n2)    #제곱(승수)

# %연산 활용(나머지 연산) 부분

test = 5
print(test % 2 == 0) #홀수 짝수 구분

print(test % 5 == 0) #5배수 구분

print(test % 6 + 1)
# test 값이 어떤 수라도 1~6사이 값만 출력
# 숫자의 범위 제한에 사용

test = 1234    #숫자의 자리수 구분
print(test % 10) #test 값에서 뒤의 한자리만 출력하기
print(test % 100) #test 값에서 뒤의 2자리만 출력하기
print(test % 1000) #test 값에서 뒤의 3자리만 출력하기

#2. 크기 비교 연산자
n1 = 10
n2 = 3
print('n1 > n2 : ', n1 > n2) #초과
print('n1 < n2 : ', n1 < n2) #미만
print('n1 >= n2 : ', n1 >= n2) #이상
print('n1 <= n2 : ', n1 <= n2) #이하
print('n1 == n2 : ', n1 == n2) #일치
print('n1 != n2 : ', n1 != n2) #불일치

print(type(True))
print(type(False))
flag = True #변수에 저장해 뒀다가 나중에 사용 가눙
flag = n1 > n2
print(flag)