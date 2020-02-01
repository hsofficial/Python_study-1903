'''
snail 01
'''
def PrintList(li):
    for i in range(len(li)):
        for j in range(len(li[i])):
            print('{:2} '.format(li[i][j]), end='')
        print()
    print()
    
snail = []
for i in range(5):
    snail.append([0,0,0,0,0])
    
num = 0
    
# 여기서부터 숫자를 대입하는 과정
# 1. 프로그램은 상수에 대한 의존도가 낮을수록 좋다 (변수로 처리하는게 더 좋다)
# 좌표값(x,y)
# 반복횟수(길이)

x, y = 0, -1
length = 5
sign = 1


for i in range(length): #y 5 plus
    num += 1
    y += sign           #부호
    snail[x][y] = num
    
length -= 1             #길이감소
    
for i in range(length): # x 증가 (4)
    num += 1
    x += sign
    snail[x][y] = num
    
sign *= -1              #부호 반전
    
for i in range(length): # y 감소 (4)
    num += 1
    y += sign
    snail[x][y] = num

length -= 1     # 길이 감소

for i in range(length): # x 감소 (3)
    num += 1
    x += sign
    snail[x][y] = num
    
sign *= -1      # 부호 반전

for i in range(length): # y 증가 (3)
    num += 1
    y += sign
    snail[x][y] = num
    
length -= 1     # 길이 감소

for i in range(length): # x 증가 (2)
    num += 1
    x += sign
    snail[x][y] = num

sign *= -1      # 부호 반전

for i in range(length): # y 감소 (2)
    num += 1
    y += sign
    snail[x][y] = num

length -= 1     # 길이 감소

for i in range(length): # x 감소 (1)
    num += 1
    x += sign
    snail[x][y] = num
    
sign *= -1      # 부호 반전

for i in range(length): # y 증가 (1)
    num += 1
    y += sign
    snail[x][y] = num
    
# 여기까지

PrintList(snail)
