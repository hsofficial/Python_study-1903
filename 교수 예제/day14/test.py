length = 5
arr = [[0]* length for i in range(length)]


x = 0
y = length // 2
num = 0
for i in range(1, length + 1):
    num += 1
    arr[x][y] = num
    print('===arr[{}][{}]'.format(x, y))
    x -= 1
    y += 1
    if x == -1: x = 4
    if y == 5: y = 0
    #nmg = i - i * 5 // 5
    #if nmg == 0:
    if i % 5 == 0:
        x += 1
        continue
    
for i in range(5):
    for j in range(5):
        print('[{:2d}] '.format(arr[i][j]), end=' ')
    print('\n')