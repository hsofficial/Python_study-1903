'''
ex02.py

while과 for문
'''
# while
i = 0               # 반복의 초기값
while i < 5:        # 반복의 끝값(포함하지 않는다)
    print('Hello, world!')
    i += 1          # 반복중의 증감값
print()


# for
for i in range(0,5,1):          # for문의 기본 형식 (초기값, 끝값, 증감값)
    print('Hello, Python!')
print()

        
for i in range(0,5):            # 초기값, 끝값 (증감값은 생략되면 1로 처리)
    print('Hello, OOP!')
print()

for i in range(5):              # 끝값 (초기값은 생략되면 0으로 처리)
    print('Hello, Django!', i)
print()

facto = 1
for i in range(4, 0, -1):
    facto *= i              # facto         # i    -1
print(facto)                #  1            # 4
                            #  4            # 3
                            # 12            # 2
                            # 24            # 1
                            # 24            # 0    # 반복 종료
                            
# 1. for문을 이용하여 1부터 100까지의 합을 구하세요

total = 0
for i in range(101):    # for i in range(1,101,1):
    total += i
print('1부터 100까지의 합은', total)

# 2. for문을 이용하여 itbank라는 문자열의 각 글자의 아스키 코드 합을 구하세요
#    ord('i'), len(문자열)

total = 0
word = 'itbank'
for i in range(len(word)):      # len(word) == 6, range(6) == range(0,6,1)
    total += ord(word[i])       # i : 0, 1, 2, 3, 4, 5
    
print(word,'의 각 아스키코드 합은', total)


for i in range(1,11):
    print('# ' * i)
print()

total = 0
for i in range(1,101):
    if i % 2 == 0:
        total += i
print('짝수의 합 :',total)
print()

# 문제. 사용자에게 정수를 입력받아서, 해당 수의 약수를 출력하는 코드를 작성하세요

#data = int(input('정수 입력 : '))
data = 1
for i in range(1, data + 1, 1):
    if data % i == 0:
        print(i, end=' ')
print()

# 소수 (Prime Number) : 1과 자기자신을 제외한 어떤 수로도 나누어 떨어지지 않는 수
# 소수 판별 식
'''
data = int(input('소수 판별 정수 입력 : '))
result = '소수가 맞습니다'

for i in range(2, data + 1):            # 범위에서 1을 제외한다
    if data != i and data % i == 0:     # 소수가 아닐 경우 확인(자기자신이 아닐 경우)
        result = '소수가 아닙니다'
        break

print(result)
'''
# 사용자에게 숫자를 입력받아서, 1부터 입력받은 수 사이의 소수를 출력하는 코드를 작성하세요
print('1부터 입력받은 수 사이의 소수를 출력합니다\n')
'''
data = 20   #int(input('정수 입력 : '))

for i in range(1, data + 1):        # 1부터 20중에서
    flag = True
    for j in range(2, i):           # 2부터 i이전까지(i를 포함하지 않고)
        if i != j and i % j == 0:   # i가 j로 나누어 떨어지면 flag = False(조건 탈락)
            flag = False
            break
    if flag == True:                # 조건에서 탈락하지 않았다면 출력하라
        print(i, end=' ')
'''
data = 20
for i in range(1, data + 1):        # 범위를 지정하고, 범위중 특정 숫자가 i
    flag = True
    # flag가 False인지 아닌지 검사하는 수식
    for j in range(2, i + 1):            # 범위에서 1을 제외한다
        if i != j and i % j == 0:     # 소수가 아닐 경우 확인(자기자신이 아닐 경우)
            flag = False              # 자기자신을 제외하고 나누어 떨어지면 조건 탈락
            break                     # 반복탈출(내부 for(j))
    
    if flag == True:
        print(i, end=' ')






    


















