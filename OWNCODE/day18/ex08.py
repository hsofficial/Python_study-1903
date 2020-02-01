'''
login
'''

account = {}        # 계정    , 비밀번호
account.__setitem__('iu930516', 'iu')
account.__setitem__('itbank', 'it')
account.__setitem__('test', '1')

#주어진 사전 자료형을 활용하여 비밀번호를 사용자에게 노출하지 않고,
#코드상에 비밀번호를 상수로 사용하지 않고 로그인 검증과정을 진행할 수 있는 함수 제작

def Login(id, pw):
    if account.get(id) != None: # id 존재
        if account.get(id) == pw:   #pw 존재
            print('로그인 성공')
        else:
            print('비밀번호 재확인 필요')
    else:
        print('계정 재확인 필요')
        
Login(input('id : '), input('pw : '))