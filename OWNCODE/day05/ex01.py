'''
ex01.py

'''

# 연산자 활용 문제 
#1. 정수를 입력받아서 입력받은 수가 3의 배수이면 T, 아니면  F 출력

number1 = int(input('정수 입력 :'))
answer1 = number1 % 3
flag1 = answer1 == 0
print(flag1)

'''
모범답안
print(var1 % 3 == 0) #크기 비교의 결과는 논리형으로 나타남
'''

#2. 정수를 입력받아서 입력받은 수가 4의 배수이면서 동시에 7의 배수이면 T 아니면 F

number2 = int(input('정수 입력 :'))
answer2_1 = number2 % 4
answer2_2 = number2 % 7
flag2_1 = answer2_1 == 0
flag2_2 = answer2_2 == 0
flag2_3 = (flag2_1 == flag2_2)
print(flag2_3)

'''
모범답안
print(var2 % 4 == 0 and var2 % 7 == 0) #논리 연산의 결과도 논리형으로 나타난다
'''

#3. 입력받은 수가 0에서 100사이 수이면 T 아니면 F 

number3 = int(input('정수 입력 (0 ~ 100) :'))
answer3 = ( (number3 >= 0) and (number3 <= 100) )
print(answer3)

'''
모범답안
print(0<= var3 and var3 <= 100) #0 <= var3 <= 100  >>> 단순계산은 되지만 if문 사용불가
'''