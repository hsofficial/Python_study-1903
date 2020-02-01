'''
ex04.py

while
'''
#while 활용 a 부터 z까지의 알파벳 한줄에 출력, 알파벳은 띄워쓰기로 구분
#글자는 ascii code 에 의해서 수로 다루어짐 ord('a')
#ascii code 해당 숫자는 chr(97)에 의해서 지정된숫자로 출력

ch = ord('A')           #ch에는 a ascii code 정수로 대입
while ch <= ord('Z'):   #z의 ascii code값보다 작거나 같을때까지
    print(chr(ch), end=' ')
    ch += 1
print()
    
#q1. 1~100사이 7배수 한줄 출력

num = 1
while num < 15:
    print(num * 7, end=' ')
    num += 1
print()
    
#q2) 10~0까지 콤마 구분 한줄 출력

num1 = 10
while num1 >= 0:
    print(num1, end = (num1 == 0) and '\n' or ', ')
    num1 -= 1
print()
    
#q3) life is too short you need python 입력받은 횟수만큼 출력

cnt = int(input('반복 횟수 입력'))

while cnt != 0:
    print('life is too short you need python')
    cnt -= 1
    
#q4) 위 문자열을 한글자씩 ,로 구분하여 출력
#반복횟수 : 문자열의 길이(len(text))

text = 'life is too short you need python'
cnt = len(text)
i = 0
while i < cnt:
    print('[', text[i], ']', end = (i == cnt - 1)and '\n' or ', ', sep='' )
    i += 1