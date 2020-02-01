'''
ex03.py
함수의 가변인자
'''

def printall(*args):
    print(args)
    
printall(1,2,3)
printall(1,2,3,4,5)

#함수 호출시 인자의 개수를 다양하게 지정할 수 있음

def Total(*score):          #여러개의 인자 전달
    total = 0               #숫자를 합산할 total 변수를 0으로 초기화
    str1 = ''               #문자열을 합산할 str 변수 '' 초기화
    for i in score:         #전달받은 score 중에서 하나를 i 로 지정하고 반복
        if type(i) == int:  
            total += i
        if type(i) == str:
            str1 += i
    if str1 != '' :         #str1에 어떤 값이 더해져서 빈값이 아니면
        total = str1        #total을 str1로 바꿈
    return total

print(Total(1,2,3,4,5,6,7,8,9))
print(Total('dlwlrma ','dlwldms ','dlwlehd '))
