'''
ex04.py

함수의 매개변수 기본값 설정
'''

def Profile(name = '이름없음', age = 0):
    print('{}님의 나이는 {}살입니다'.format(name, age))
    
Profile('이지은', 27)
# Profile('이지은')    # 인자를 전달하지 않아서, 매개변수가 비어있으므로 처리할 수 없다
Profile('이지은')
Profile()

# 1. 이름과 직업을 전달받아서 출력하는 함수 Func()를 작성하세요
# (단, 직업을 전달하지 않으면 '무직'이라고 출력하도록 설정하세요)
def Func(name, job = '무직'):
    print('{}님의 직업은 {}입니다'.format(name, job))

Func('주호민', '웹툰작가'); Func('이말년')

# 예시) 저장할 파일 이름을 설정할 때, 이름을 따로 지정하지 않으면 untitled.txt로 저장하고
#      이름을 지정하면 지정한이름.txt





