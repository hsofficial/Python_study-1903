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
    
# 여기서부터 숫자를 대입하는 과정            # 길이 : 5 - 4 - 4 - 3 - 3 - 2 - 2 - 1 - 1
#     x [y]   +    5                         # 좌표 : y - x - y - x - y - x - y - x - y
snail[0][0] = 1                              # 증감 : +   +   -   -   +   +   -   -   +
snail[0][1] = 2                              # 값    : num += 1
snail[0][2] = 3
snail[0][3] = 4
snail[0][4] = 5

#    [x] y    +    4
snail[1][4] = 6
snail[2][4] = 7
snail[3][4] = 8
snail[4][4] = 9

#     x [y]   -    4
snail[4][3] = 10
snail[4][2] = 11
snail[4][1] = 12
snail[4][0] = 13

#    [x] y    -    3
snail[3][0] = 14
snail[2][0] = 15
snail[1][0] = 16

#     x [y]   +    3
snail[1][1] = 17
snail[1][2] = 18
snail[1][3] = 19

#    [x] y    +    2
snail[2][3] = 20
snail[3][3] = 21

#     x [y]   -    2
snail[3][2] = 22
snail[3][1] = 23

#    [x] y    -    1
snail[2][1] = 24

#     x [y]   +    1
snail[2][2] = 25

# 여기까지

PrintList(snail)
