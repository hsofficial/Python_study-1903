'''
snail
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


    
PrintList(snail)

'''
     1  2  3  4  5
    16 17 18 19  6 
    15 24 25 20  7
    14 23 22 21  8
    13 12 11 10  9
'''





