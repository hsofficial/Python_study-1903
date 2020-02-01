'''
ex01.py

'''

# 연산자 활용 문제

# 1. 정수를 입력받아서, 입력받은 수가 3의 배수이면 True, 아니면 False를 출력하는 코드를 작성하기

var1 = int(input('정수 입력 : '))
print(var1 % 3 == 0)        # 크기 비교의 결과는 논리형(bool)로 나타난다


# 2. 정수를 입력받아서, 입력받은 수가 4의 배수이면서 동시에 7의 배수이면 True, 아니면 False

var2 = int(input('정수 입력 : '))
print((var2 % 4 == 0) and (var2 % 7 == 0))  # 논리 연산의 결과도 논리형(bool)으로 나타난다

# 3. 입력받은 수가 0에서 100 사이의 수이면 True, 아니면 False

var3 = int(input('정수 입력 (0 ~ 100) : '))
print(0 <= var3 and var3 <= 100)        # 0 <= var3 <= 100        (X)













