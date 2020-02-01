'''
ex04.py

if의 중첩 (중첩된 if문)
'''

data = int(input('정수 입력 : '))

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
if A:        A 조건이 참이면
    if B:        B 조건도 참이면 => if A and B:
        print('A and B')
'''
    
sid = 'itbank'      # 프로그램이 알고있는 준비된 데이터
spw = 'it'

uid = input('ID : ')    # 사용자에게 입력받는 데이터
upw = input('PW : ')
    
if sid == uid:
    if spw == upw:          # ID도 일치하고 PW도 일치하면
        print('로그인 성공 !!')
    else:
        print('비밀번호가 일치하지 않습니다')
else:
    print('계정을 찾을 수 없습니다')
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    