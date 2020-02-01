'''
ex04.py

문자열 관련 함수
'''

word = 'you nEEd python'
print('문자열의 길이 :', len(word))
print('문자열에서 원하는 글자가 있는가 :', word.find('p'))    # 있으면 index를 반환
print('문자열에서 원하는 글자가 있는가 :', word.find('1'))    # 없으면 -1
print('문자열이 숫자로 구성되었는가 :', word.isnumeric())
print('문자열이 숫자로 구성되었는가 :', '1234'.isnumeric())
print('문자열이 영문자로 구성되었는가 :', word.isalpha())     # 띄워쓰기는 영문자로 판단하지 않는다
print('문자열을 대문자로 변경 :', word.upper())
print('문자열을 소문자로 변경 :', word.lower())
print('문자열의 첫 글자만 대문자로 변경 :', word.capitalize())
