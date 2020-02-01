'''
login
'''
account = {}        # 계정    , 비밀번호
account.__setitem__('iu930516', 'iu')
account.__setitem__('itbank', 'it')
account.__setitem__('test', '1')

# 주어진 사전 자료형을 활용하여 비밀번호를 사용자에게 노출하지 않고,
# 코드상에 비밀번호를 상수로 사용하지 않고, 로그인 검증과정을 진행할 수 있는 함수를 제작하세요

def Login(id, pw):
    if account.get(id) != None: # id가 존재한다
        if account.get(id) == pw: # pw가 일치한다
            print('로그인 성공')
        else:
            print('비밀번호를 다시 확인해주세요')
    else:
        print('계정을 다시 확인해주세요')

Login(input('ID : '), input('PW : '))
        
        
        
        
        
