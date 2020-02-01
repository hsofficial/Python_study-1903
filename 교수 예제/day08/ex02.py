'''
ex02.py

사용자에게 숫자를 입력받으려는데, 숫자가 아닌 값을 입력하거나, 입력을 하지않고 엔터를 누르면 ??
'''

'''
num = int(input('정수 입력 : '))    # 일반적인 정수입력 구문이지만, 입력을 잘못하면 예외가 발생한다
print('num :', num)
'''

num = input('정수 입력 : ')

if num.isdigit():   num = int(num)              # 만약 num이 숫자로 구성되었으면 숫자로 변환
else:               print('입력값이 정수가 아닙니다') # 아니면 입력값이 정수가 아닙니다 라고 출력
    
print('num :', num) # 숫자라면 숫자형태로 변환되어있고, 아니면 문자열의 형태로 남아있다
print('type(num) : ', type(num))
if type(num) == str:     print('ord(num) : ', ord(num))
