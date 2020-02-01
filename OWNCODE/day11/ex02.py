'''
ex02.py

문자열 관련  함수 예제
'''

formular = input('덧셈 포함 수식 입력 : ')
flag = formular.find('+')
text = ""

print(flag)
for i in range(len(formular)):
    if formular[i] != ' ':
        text += formular[i]
        
print('띄워쓰기 제외 글자 = ', text)

count = text.count('+')
print(print('덧셈 기호의 개수 : ', count))

list1 = []
list1 = text.split('+')     # list1 = [1, 2, 3]
print(list1)
total = 0
for i in range(len(list1)):
    total += int(list1[i])  # i = 0, total = 1 / i = 1, total = 1 + 2 / i = 2 ...
print(total)