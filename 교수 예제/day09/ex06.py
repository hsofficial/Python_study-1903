'''
반복문 개념 기초
'''

# 1. 1부터 10까지 출력하기

i = 1
while i <= 10:
    print(i, end=' ')
    i += 1
print()

# 2. 1부터 10사이의 홀수만 출력하기

i = 1
while i <= 10:
    if i % 2 != 0:  # 홀수의 조건
        print(i, end=' ')
    i += 1
print()

# 3. 1부터 10사이의 짝수만 출력하기

i = 1
while i <= 10:
    if i % 2 == 0:  # 짝수의 조건
        print(i, end=' ')
    i += 1
print()


# 4. 홀수의 합

total = 0       # 빈 통
i = 1
while i <= 10:
    if i % 2 != 0:  # 홀수의 조건
        total += i
    i += 1
print('홀수의 합 :', total)

# 5. 짝수의 합

total = 0       # 빈 통
i = 1
while i <= 10:
    if i % 2 == 0:  # 짝수의 조건
        total += i
    i += 1
print('짝수의 합 :', total)


# 문자열 5번 출력하기

print('Hello, world!')
print('Hello, world!')
print('Hello, world!')
print('Hello, world!')
print('Hello, world!')
print()

i = 0
while i < 5:
    print("Hello, Python")
    i += 1





















