'''
ex02.py

리스트 정렬
오름차순 : 점점 커지는 순서대로 정렬        _--￣
내림차순 : 점점 작아지는 순서대로 정렬                ￣--_
'''

list1 = [4,2,8,6,7]

print(list1)

for i in range(len(list1)):
    for j in range(i, len(list1)):
        if list1[i] > list1[j]:
            tmp = list1[i]   # 대입 연산자 : 우변의 값을 좌변의 변수공간에 복사하여 대입한다
            list1[i] = list1[j]
            list1[j] = tmp

print(list1) 

list2 = [4,2,8,6,7]
list2.sort()    # 오름차순 정렬
print(list2)
list2.sort(reverse=True)    # 내림차순 정렬
print(list2)
print()

list3 = ['원빈', '강동원', '하정우', '이준기']
print(list3)
list3.sort()
print(list3)
list3.sort(reverse=True)
print(list3)
print('\n\n\n')

# 문제 1. 5개의 숫자를 임의로 입력받아서 오름차순으로 정렬하여 출력하세요
# 입력) 5, 8, 100, -5, 50
# 출력) -5, 5, 8, 50, 100

list1 = [0,0,0,0,0]
for i in range(len(list1)):
    list1[i] = int(input('숫자 입력 : '))
print(list1)    # 정렬전
list1.sort()
print(list1)    # 정렬후

print()
# 문제 2. 5명의 이름과 나이를 입력받아서 내림차순으로 정렬하여 출력하세요

name = []
age = []

for i in range(5):
    name.append(input('이름을 입력하세요 : '))
    age.append(int(input('나이를 입력하세요 : ')))
    print()
    
print('이름 :', name)
print('나이 :', age)

for i in range(len(age)):
    for j in range(i, len(age)):
        if age[i] < age[j]:     # 나이를 기준으로 정렬할 때
            tmp = age[i]        # 나이도 바꿔주고
            age[i] = age[j]
            age[j] = tmp
            
            tmp = name[i]       # 같은 인덱스(같은 위치)의 이름도 변경해준다
            name[i] = name[j]
            name[j] = tmp

print()
print('이름 :', name)
print('나이 :', age)




















