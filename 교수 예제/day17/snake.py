'''
snake
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





