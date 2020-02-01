'''
ex03.py

함수의 가변인자
'''

def PrintAll(*args):
    print(args)
    
PrintAll(1,2,3)
PrintAll(4,5,6,7,8,9)
PrintAll('hello','python')

# 함수 호출시 인자의 개수를 다양하게 지정할 수 있다 

def Total(*score):          # 여러개의 인자를 전달받아서
    total = 0               # 숫자를 합산할 total 변수를 0으로 초기화
    str1 = ''               # 문자열을 합산할 str1 변수를 ''으로 초기화
    for i in score:         # 전달받은 score중에서 하나를 i라고 지정하고 반복
        if type(i) == int:  # 만약 i의 자료형이 정수라면
            total += i          # total에 더한다
        if type(i) == str:  # 만약 i의 자료형이 문자열이라면
            str1 += i           # str1에 더한다
    if str1 != '':          # str1에 어떤 값이 더해져서 빈값이 아니면
        total = str1            # total을 str1로 바꾼다
    return total            # total을 반환한다

print(Total(1,2,3,4))
print(Total(1,2,3,4,5,6,7,8,9,10))
print(Total('You', 'Need', 'Python'))


print(range(10))
print(range(1, 10))
print(range(1, 10, 2))





