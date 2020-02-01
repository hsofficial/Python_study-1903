'''
ex02.py

문자열 관련 함수 예제
'''
#formular = "1 + 2"
formular = input('덧셈을 포함한 수식을 입력하세요 : ')
text = ""

for i in range(len(formular)):
    if formular[i] != ' ':
        text += formular[i]

print('띄워쓰기를 제외한 글자 :', text)

count = text.count('+')
print('덧셈기호의 개수 :', count)

list1 = []                  
list1 = text.split('+')     # list1 = [1, 2, 3]
print(list1)
total = 0
for i in range(len(list1)): # 
    total += int(list1[i])  # i = 0, total = 1 / i = 1, total = 1 + 2 / i = 2, total = 6
print(total)
