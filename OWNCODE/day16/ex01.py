'''
ex01.py
'''

#리스트 : 여러 데이터를 관리하기 위해서 파이썬에서 사용하는 확장 자료형
#1. 서로 다른 자료형도 묶어서 관리 할 수 있음
#2. 순번(인덱스)에 의해서 자료 관리
#3. 리스트 내에 또다른 인덱스 삽입 가능
#4. 리스트 인덱싱과 문자열 인덱싱은 거의 유사
#5. 리스트가 가지는 특정함수들이 다양한 기능을 자체 지원함

list1 = []  #리스트 선언 >>> 여러 데이터를 담을 수 있는 변수의 묶음
list1 = [100, 99, 87]   #리스트 내의 member 변수에 원하는  값을 넣을 수 있음
print('리스트 길이 : ', len(list1))
list1.append(86)
list1.append(92)
print('리스트 길이 : ', len(list1))
print('리스트 : ', list1)
print('리스트 1번째 값 : ', list1[0]) #member 변수, index 이용 접근
print('리스트 2번째 값 : ', list1[1])
print('리스트 3번째 값 : ', list1[2])
print('리스트 4번째 값 : ', list1[3])
print('리스트 5번째 값 : ', list1[4])
print()

for i in range(len(list1)):
    print('list[{}] : {}'.format(i, list1[i]))
print()

for i in list1: #길이 상관없이 list1의 모든 member 한번씩 접근
    print(i)
print()

total = 0
for i in list1:
    total += i
print('total : ', total)