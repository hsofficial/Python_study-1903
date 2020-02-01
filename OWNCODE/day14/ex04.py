'''
함수의 매개변수 기본값 설정
'''

def Profile(name = '이름없음', age = 0):
        print('{} 님의 나이는 {}살'.format(name, age))
        
Profile('아이유', 27)
Profile('아이유')

#이름과 직업을 전달받아서 출력하는 함수 Func() 직업 전달하지 않으면 무직으로 출력

def Func(name, state = '무직'):
        print('{} 님의 직업은 {}'.format(name, state))
        
Func('qwerty'); Func('123456', '234567')