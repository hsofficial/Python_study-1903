'''
snail
'''

def PrintList(li):
    for i in range(len(li)):
        for j in range(len(li[i])):
            print('{:2} '.format(li[i][j]), end='')
        print()
    print()
    
snake = []
for i in range(5):
    snake.append([0,0,0,0,0])
    
num = 0
for i in range(5):
    if i % 2 == 0:
        for j in range(0,5,1):
            num += 1
            snake[i][j] = num
    else:
        for j in range(4,-1,-1):
            num += 1
            snake[i][j] = num
    
PrintList(snake)

'''
     1  2  3  4  5
    10  9  8  7  6 
    11 12 13 14 15
    20 19 18 17 16
    21 22 23 24 25
'''

snail = []
for i in range(5):
    snail.append([0,0,0,0,0])
    
length = 5
pm = 1
x = 0
y = -1
num = 0
while True:
    for i in range(length):
        num += 1
        y += pm
        snail[x][y] = num   
    length -= 1
    for i in range(length):
        num += 1
        x += pm
        snail[x][y] = num
    break
 
'''   
for i in range(5):
    snail[0][i] = i + 1
for j in range(4):
    snail[j][4] = j + 1
for i in range(4):
    snail[4][i] = i - 1
for j in range(3):
    snail[j][0] = j + 1
for i in range(2):
    snail[1][i] = i + 1
for j in range(2):
    snail[j][3] = j + 1

1 [0, 0]
2 [0, 1]
3 [0, 2]
4 [0, 3]
5 [0, 4] 
길이 감소

6 [1, 4] 
7 [2, 4] 
8 [3, 4] 
9 [4, 4] 
부호 반전

10 [4, 3]
11 [4, 2]
12 [4, 1]
13 [4, 0]
길이 감소

14 [3, 0]
15 [2, 0]
16 [1, 0]
부호 반전

17 [1, 1]
18 [1, 2]
19 [1, 3]
길이 감소

20 [2, 3]
21 [3, 3]
부호 반전

22 [3, 2]
23 [3, 1]
길이 감소

24 [2, 1]
부호 반전

25 [2, 2]
길이 0이 되면 종료
''' 
PrintList(snail)

'''
     1  2  3  4  5
    16 17 18 19  6 
    15 24 25 20  7
    14 23 22 21  8
    13 12 11 10  9
'''