# day03-ex01.py
# Ctrl + F5 = Run (VS)
# Ctrl + B = 파일 탐색기 숨기거나 열기 (VS)
# Ctrl + F5 = 실행 결과창 숨기거나 열기 (VS)

from os import system
system("cls")
#VS 전용 창 정리 명령어

name = input('이름 입력 : ')
age = int(input('나이 입력 : '))

year = 2019 - age + 1

print(name, '님은', year, '년생이며', age, '세 입니다')