'''
2자원 리스트
'''

list1 = [1,2,3,4,5]

list2=[[1,2,3],[4,5,6],[7,8,9]]

list3=[
        [1,2,3],
        [4,5,6],
        [7,8,9]
      ]

for i in range(3):
    for j in range(3):
        print('{:2d} '.format(list2[i][j]), end='')#i 세로 먼저 j 가로 나중
    print()
print()    

for i in range(3):
    for j in range(3):
        print('{:2d} '.format(list3[i][j]), end='')
    print()
print()

list4 = []
for i in range(5):
    list4.append([0,0,0,0,0])

for i in range(len(list4)):
    for j in range(len(list4[i])):
        print('{:2d} '.format(list4[i][j]), end='')
    print()
print()

num = 0
# list4에 순서대로 1에서 25까지의 정수를 대입하기
for i in range(len(list4)):
    for j in range(len(list4[i])):
        num += 1
        list4[i][j] = num

for i in range(len(list4)):
    for j in range(len(list4[i])):
        print('{:2d} '.format(list4[i][j]), end='')
    print()
print()