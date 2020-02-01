'''
ex01.py

연산자 : 산술연산, 크기비교, 논리연산, 대입연산(복합대입), 비트연산
'''
a = True
b = False       # bool : True 나 False, 참과 거짓을 표현하는 자료형
                # 삼항 연산의 조건, if, while 등등의 제어문의 조건으로 활용된다

# 1. 논리 값은 다른 논리값과 연산하여 다른 결과를 나타낼 수 있다

cash, card = 0, 0
canGoHome = cash >= 1200 or 0 >= 1200
print('현금 :', cash, '카드 잔액 :', card, '->', canGoHome, '\n')

cash, card = 1500, 0
canGoHome = cash >= 1200 or card >= 1200
print('현금 :', cash, '카드 잔액 :', card, '->', canGoHome, '\n')

cash, card = 1000, 5000
canGoHome = cash >= 1200 or card >= 1200
print('현금 :', cash, '카드 잔액 :', card, '->', canGoHome, '\n')

cash, card = 50000, 50000
canGoHome = cash >= 1200 or card >= 1200
print('현금 :', cash, '카드 잔액 :', card, '->', canGoHome, '\n')


age, gender = 15, '남자'
GoArmy = (age >= 19) and (gender == '남자')
print('나이 :', age, '성별 :', gender, '->', GoArmy, '\n')

age, gender = 16, '여자'
GoArmy = (age >= 19) and (gender == '남자')
print('나이 :', age, '성별 :', gender, '->', GoArmy, '\n')

age, gender = 24, '남자'
GoArmy = (age >= 19) and (gender == '남자')
print('나이 :', age, '성별 :', gender, '->', GoArmy, '\n')

age, gender = 22, '여자'
GoArmy = (age >= 19) and (gender == '남자')
print('나이 :', age, '성별 :', gender, '->', GoArmy, '\n')


print('\n\n')

gender = '남자'
flag = gender == '남자'
print('성별 :', gender, '->', not(flag) and '입장 가능' or '입장 불가')

gender = '여자'
flag = gender == '남자'
print('성별 :', gender, '->', not(flag) and '입장 가능' or '입장 불가')

gender = '123'
flag = gender == '남자'
print('성별 :', gender, '->', not(flag) and '입장 가능' or '입장 불가')
    

'''
    논리연산자는 bool값의 변화를 가져오며
    and : 서로 다른 두개 이상의 논리값이 모두 참이여야 결과가 참이 나온다
    or : 서로 다른 두개 이상의 논리값 중에서 하나만 참이여도 결과가 참이 나온다
    not : 논리값의 결과를 반전시킨다(True->False, False->True)
''' 
a = True
b = False
c = True
print(a and b and c)    # True and False and True
print(a or b or c)      # True or False or True
print(not(a or b or c)) 

number = int(input('정수 입력 : '))
print(number and True or False)
'''
    1,2,3,4.... : True        있다
    0 : False                없다
    -1, -2, -3, -4 : True    있다
'''








