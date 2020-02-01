'''
ex02.py
사용자에게 숫자 입력시 숫자 아닌 값 혹은 미입력 상태  enter
'''

'''
num = int(input('정수 입력 : '))    #일반적인 정수 입력 구문, 입력 오류시 예외 발생
print('num', num)
'''

num = input('정수 입력 :')

if num.isdigit():
    num = int(num)  #num 숫자면 숫자 변환
    
else:
    print('입력값 정수 아님')  #숫자 아니면 오류 출력
    
print('num:', num) #숫자라면 숫자형태 아니면 문자열의 형태로 남음
print('type(num) : ', type(num))

if type (num) == str:
    print('ord(num) : ', ord(num))