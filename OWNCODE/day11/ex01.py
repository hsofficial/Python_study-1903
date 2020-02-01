'''
ex01.py
제어문 정리
'''

#1. 이름과 생년월일을 입력받아 나이와 미성년자 여부 판단 메뉴형 프로그램 작성

name = ""
age = 0
adult = ""

while True:
    print('1.이름 입력')
    print('2. 생년월일 입력')
    print('3. 결과 확인')
    print('0. 종료')
    print('=' * 20)
    menu = input('메뉴 선택 : ')
    print()
    
    if menu == '1' :
        name = input('이름 : ')
        
    elif menu == '2' :
        birth = input('생년월일 입력 YYMMDD : ')
        year = int(birth[:2])
        year += (year > 19) and 1900 or 2000
        age = 2019 - year + 1
        adult = (age >= 20) and '성인 ' or '미성년자'
        
    elif menu == '3' :
        
        if name == "" or age == 0 or adult == "":   # 하나라도 빈 값이면 경고
            print('[모든 값을 입력해야 결과를 출력할 수 있음]\n')
            
        else:                                       # 모든 값이 준비되었다면
            print('{}님의 나이는 {}살, {}\n'.format(name, age, adult))
        
    elif menu == '0' :
        print('[프로그램 종료]\n')
        break   # break는 반복문을 아래로 탈출하는 기능을 가진다
    
    else:
        print('[메뉴 잘못 선택]\n')