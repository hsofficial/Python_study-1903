'''
ex02.py
list 정렬
오름차순 : 커지는 순서대로    123
내림차순 : 작아지는 순서대로    321
'''

list1 = [2,4,8,6,7]

print(list1)

for i in range(len(list1)):
    for j in range(i, len(list1)):
        if list1[i] > list1[j]: #방향설정 오름차순 내림차순
            tmp = list1[i]   #대입 연산자 : 우변의 값을 좌변의 변수 공간에 복사하여 대입
            list1[i] = list1[j]
            list1[j] = tmp
            
print(list1)

print()

list2 = [2,4,8,6,7]
list2.sort()
print(list2)    #오름차순
list2.sort(reverse = True)
print(list2)    #내림차순

print()

list3 = ['원빈','강동원','하정우','이준기']
list3.sort()
print(list3)    #오름차순
list3.sort(reverse = True)
print(list3)    #내림차순

print('\n\n\n')

#문제 1. 5개 숫자 임의 입력받아 오름차순 정렬 출력
list4 = [0,0,0,0,0]
for i in range(len(list4)):
    list4[i] = int(input('정수 입력 : '))
list4.sort()
print(list4)    #오름차순

#문제 2. 5명의 이름과 나이 입력받아 내림차순 정렬 출력
list5 = []
list6 = []
for i in range(5):
    list5.append(input('이름 입력 : '))
    list6.append(int(input('나이 입력 : ')))
    print()
        
print('이름', list5)
print('나이', list6)

for i in range(len(list6)):
    for j in range(i, len(list5)):
        
        if list6[i] < list6[j]: #나이 기준 정렬
            temp = list6[i]     #나이 변경
            list6[i] = list6[j]
            list6[j] = tmp
            
            temp = list5[i]     #같은 인덱스(위치) 이름 변경
            list5[i] = list5[j]
            list5[j] = tmp
            
print()   
print('이름', list5)
print('나이', list6)            
    

