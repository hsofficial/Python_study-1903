'''
ex03.py

ASCII Code : American Standard Code for Information Interchange 

1. 미국 표준이므로 한글이나 다른 외국어는 포함되어 있지 않다
2. 공백, Null, ESC, 엔터, 기타 키들의 값도 가지고 있다
3. 숫자, 영문자, 기본특수기호 등을 포함한다
4. 128개의 문자를 표현하며 7 bit로 구성
'''

data = input('문자를 한 글자만 입력하세요 : ')
if len(data) == 1: print('ord(data) :', ord(data))
print()

num = int(input('아스키 코드를 입력하세요 : '))
print('chr(num) : ', chr(num))
print('test')

