'''
ex04.py

while
'''
# while문을 활용하여, A부터 Z까지의 알파벳을 한줄에 출력하세요, 각 알파벳은 띄워쓰기로 구분하세요

#    글자는 ASCII Code에 의해서 숫자로 다루어진다 ord('a')
#    아스키 코드에 해당하는 숫자는 chr(97)에 의해서 지정된 문자로 출력할 수 있다
#    정수는 덧셈이 가능하다 <-

ch = ord('A')           # ch에는 A의 아스키 코드가 정수로 대입된다
while ch <= ord('Z'):   # Z의 아스키 코드값보다 작거나 같을때까지
    print(chr(ch), end=' ')
    ch += 1
print()
 
# 문제1) 1부터 100사이의 7의 배수를 한줄로 출력하세요
cnt = 1                     # 1. cnt 초기값 1
while cnt <= 100:           # 2. cnt 가 100 이하이면 반복
    if cnt % 7 == 0:        # 3. cnt 가 7로 나누어 떨어지면 
        print(cnt, end=' ') # 4. cnt 를 출력, 줄 바꾸지 않음
    cnt += 1                # 5. if조건에 상관없이 cnt는 항상 1씩 증가
print()                     # while이 끝나면 한줄 바꿈

# 문제1) 7 * n 출력하기
cnt = 1
while 7 * cnt <= 100:
    print(cnt * 7, end=' ')
    cnt += 1
print()



# 문제2) 10에서 0까지 ,로 구분하여 한줄로 출력하기

i = 10
while i>=0:
    print(i, end=(i == 0) and ' ' or ', ')
    i -=1
print()


# 문제3) Life is too short, you need python 이라는 문자열을 입력받은 횟수만큼 출력하세요

text = 'Life is too short, you need python'
cnt = int(input('반복 횟수를 입력 : '))
i = 0
while i < cnt:
    print(text)
    i += 1 
    
# 위 문자열을 한 글자씩 , 로 구분하여 출력하세요

#    반복횟수 : 문자열의 길이 -> len(text)

text = 'Life is too short, you need python'
cnt = len(text)
i = 0
while i < cnt:
    print('[',text[i],']', end=(i == cnt - 1) and '\n' or ', ', sep='')
    i += 1













