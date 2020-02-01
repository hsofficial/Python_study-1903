'''
while / for
'''
#while

i = 0
while i < 5:
    print('hello1')
    i += 1
print()

#for

for i in range (0,5,1): #range(시작값,끝값,증감값) >>> for 기본형식
    print('hello2')
print()

for i in range (0,5): #range(시작값,끝값) >>> 중감값 1로 처리
    print('hello3')
print()

for i in range (5): #range(끝값) >>> 초기값 0 처리
    print('hello4')
print()

facto = 1
for i in range (4, 0, -1):
    facto *= i
print(facto)
print()

#for 이용 1부터 100까지 합 구하기

value = 0
for q in range(1,101,1):
    value += q
print(value)
print()

#for 이용 itbank 문자열의 각 글자 ASCII 합 구하기
#len('문자열') ord('i')

word = 'itbank'
value2_1 = len(word)
value2_2 = 0

for n in range(0, value2_1, 1):
    value2_2 += ord(word[n])
    
print(value2_2)
print()

for i in range(1,11):
    print('# ' * i)
print()

total = 0
for i in range(1,101):
    if i % 2 == 0:
        total += i
print('짝수합', total)
print()

#q. 사용자에게 정수 입력받아 해당 수의 약수 출력 코드 작성

data = 24
for i in range(1, data+1, 1):
    if data % i == 0:
        print(i, end=' ')
print(' ')

#소수(prime number) >> 약수 1과 자기자신
#소수 판별식

data = int(input('정수 입력'))
result = '소수'

for i in range (2, data+1):         #범위에서 1 제외
    if data != i and data % i == 0: #소수 아닐 경우 확인(자기자신이 아닌 수로 나누어 떨어짐)
        result = '소수 아님'
        break
    
print(result)

#사용자에세 숫자를 입력받아서 1부터 입력받은 수 사이의 소수 출력 코드 작성

data = int(input('정수 입력'))

for i in range (1, data+1): # 밤위 지정 >>> 범위중 특정 숫자가 i
    chk = True              # 소수 판별 check 논리연산 >>> false 인지 아닌지 검사
    
    for x in range(2, i):   # x 값이 1부터 1씩 증가하면서 i-1이 될때까지 반복
        
        if i % x == 0:      # i를 x로 나눈 나머지가 0
            chk = False     # chk에 False을 저장(자기자신을 제외하고 나누어 떨어지면 조건 탈락)
        break               # 반복문 종료
        
    if chk == True:         # chk 값이 False가 아니면 소수이므로 출력
        print(i, end=" ")

