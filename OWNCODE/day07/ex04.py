'''
ex04.py

if의 중첩(중첩된 if문)
'''

data = int(input('정수 입력:'))

if data % 2 == 0:
    if data % 3 == 0:
        print('2와 3의 공배수')
    else:
        print('2의 배수')
elif data % 3 == 0:
    print('3의 배수')
else:
    print('2나 3의 배수가 아님')
    
'''
if a:                    a조건 참
    if b:                b조건 참 >>> if a and b:
        print('a and b')
'''
    
server_id = 'itbank'
server_pw = 'it'

user_id = input('ID : ')
user_pw = input('PW : ')

if server_id == user_id:
    if server_pw == user_pw:
        print('로그인 성공')
    else:
        print('비밀번호 오류')
else:
    print('미가입 계정')