'''
ex01.py
'''

# 리스트 : 여러 데이터를 한번에 관리하기 위해서 파이썬에서 사용하는 확장 자료형
#
# 1. 서로 다른 자료형도 묶어서 관리할 수 있다
# 2. 순번(index)에 의해서 자료를 관리한다
# 3. 리스트 내에 또다른 리스트를 넣을 수 있다
# 4. 리스트의 인덱싱과 문자열의 인덱싱은 거의 유사하다
# 5. 리스트가 가지는 특정 함수들이 다양한 기능을 자체 지원한다

list1 = []  # 리스트를 선언, 여러 데이터를 담을 수 있는 변수의 묶음
list1 = [100, 99, 87]   # 리스트 내의 멤버 변수에 원하는 값을 넣을 수 있다
print('list1의 길이 :', len(list1))
list1.append(86)
list1.append(92)
print('list1의 길이 :', len(list1))
print('list1 :', list1)
print('list1의 첫번째 값 :', list1[0])   # 멤버 변수, index를 이용하여 접근한다
print('list1의 두번째 값 :', list1[1])
print('list1의 세번째 값 :', list1[2])
print('list1의 네번째 값 :', list1[3])
print('list1의 다섯번째 값 :', list1[4])
print()

for i in range(len(list1)):
    print('list1[{}] : {}'.format(i, list1[i]))
print()

for i in list1: # 길이에 상관없이(순번에 상관없이) list1의 모든 멤버를 한번씩 접근하고자 할 경우
    print(i)
print()

total = 0
for i in list1:
    total += i
print('total :', total)    
    
    
    
    
    




