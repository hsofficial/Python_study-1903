'''
달팽이 2단계
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
# 여기서부터 숫자를 대입하는 과정            # 길이 : 5 - 4 - 4 - 3 - 3 - 2 - 2 - 1 - 1
                                # 좌표 : y - x - y - x - y - x - y - x - y
                                # 증감 : +   +   -   -   +   +   -   -   +
                                # 값    : num += 1
#     x [y]   +    5            
'''
snail[0][0] = 1                 
snail[0][1] = 2                 
snail[0][2] = 3
snail[0][3] = 4
snail[0][4] = 5
'''
num = 0
for i in range(0,5,1):
    num += 1
    snail[0][i] = num
    

#    [x] y    +    4
'''
snail[1][4] = 6
snail[2][4] = 7
snail[3][4] = 8
snail[4][4] = 9
'''
for i in range(1,5,1):
    num += 1
    snail[i][4] = num

#     x [y]   -    4
'''
snail[4][3] = 10
snail[4][2] = 11
snail[4][1] = 12
snail[4][0] = 13
'''
for i in range(3,-1,-1):
    num += 1
    snail[4][i] = num

#    [x] y    -    3
'''
snail[3][0] = 14
snail[2][0] = 15
snail[1][0] = 16
'''
for i in range(3,0,-1):
    num += 1
    snail[i][0] = num

#     x [y]   +    3
'''
snail[1][1] = 17
snail[1][2] = 18
snail[1][3] = 19
'''
for i in range(1,4,1):
    num += 1
    snail[1][i] = num

#    [x] y    +    2
'''
snail[2][3] = 20
snail[3][3] = 21
'''
for i in range(2,4,1):
    num += 1
    snail[i][3] = num

#     x [y]   -    2
'''
snail[3][2] = 22
snail[3][1] = 23
'''
for i in range(2,0,-1):
    num += 1
    snail[3][i] = num

#    [x] y    -    1

snail[2][1] = 24


#     x [y]   +    1
snail[2][2] = 25

# 여기까지

PrintList(snail)
