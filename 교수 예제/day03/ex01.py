'''
ex01.py
생년월일>나이

'''

name = input('이름 입력 : ')
birth = int(input('생년월일(6자리)입력  : '))

# 아이유 생일 930516

year = birth // 10000
year += (year > 19) and 1900 or 2000
#year 값이 19보다 크면 1900 더하기 아니면 2000 더하기

age = 2019 - year + 1

print(name, '님의 나이는', age, '세 입니다')
