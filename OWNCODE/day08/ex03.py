'''
ex03.py

American Standard Code for Information Interchange

1. 미국 표준이므로 한글이나 다른 외국어는 포함하지 아니함
2. 공백, null, esc, enter, 기타 키들의 값도 가짐
3. 슷자, 영문자, 기본특수기호 포함
4. 128개 문자 표현 (7bit)
'''

data = input('문자를 한 글자만 입력하시오')
if len(data) == 1: print('ord(data)', ord(data))

num = int(input('ascii code 입력'))
print('chr(num)', chr(num))