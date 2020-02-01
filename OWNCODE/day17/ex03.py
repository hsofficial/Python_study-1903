'''

ex03.py

'''

test = [
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0]
        ]

def PrintList(li):
    for i in range(len(li)):
        for j in range(len(li[i])):
            print('{:2} '.format(li[i][j]), end='')
        print()
    print()
    
PrintList(test)

'''
test[0][0] = 1
test[0][1] = 2
test[0][2] = 3
test[0][3] = 4
test[0][4] = 5
'''

for i in range(5):
    test[0][i] = i + 1

'''    
test[1][0] = 6
test[1][1] = 7
test[1][2] = 8
test[1][3] = 9
test[1][4] = 10
'''
    
for i in range(5):
    test[1][i] = (1 * 5) + (i + 1)
    
PrintList(test)
    
for i in range(5):
    for j in range(5):
        test[i][j] = (i * 5) + (j + 1)

PrintList(test)

test = [
        ['  ','  ','  ','  ','  '],
        ['  ','  ','  ','  ','  '],
        ['  ','  ','  ','  ','  '],
        ['  ','  ','  ','  ','  '],
        ['  ','  ','  ','  ','  ']
        ]

PrintList(test)

for i in range(5):
    for j in range(5):
        print('[{}, {}] '.format(i, j), end='')
    print('\n')
print('\n')

'''
test[0][0] = '* '
test[1][0] = '* '
test[1][1] = '* '
test[2][0] = '* '
test[2][1] = '* '
test[2][2] = '* '
test[3][0] = '* '
test[3][1] = '* '
test[3][2] = '* '
test[3][3] = '* '
test[4][0] = '* '
test[4][1] = '* '
test[4][2] = '* '
test[4][3] = '* '
test[4][4] = '* '
'''

for i in range(5):
    for j in range(5):
        if i >= j:
            test[i][j] = '* '


PrintList(test)
        