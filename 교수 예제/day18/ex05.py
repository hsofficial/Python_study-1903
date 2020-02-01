'''
ex05.py

Dictionary (사전 자료형) : key와  value를 하나의 묶음으로 저장하는 자료형
'''
dict1 = {1111 : 'kgitbank', 'itbank':'it'}
# 변수 = { key1 : value1, key2 : value2 ... }
# get(key) 함수를 이용하여 value를 가져올 수 있으나
# get(value) 로는 key를 추출할 수 없다
# get()함수는 매개변수에 key값을 받도록 설계되어 있다
# list자료형의 index대신 key값을 사용하도록 설정되어있다

# list[i] = value
# dict.get(key) = value

print(dict1)
print(dict1.get(1111))
print(dict1.get('kgitbank'))
print(dict1.get('itbank'))
print(dict1.get('it'))

dict2 = {}
dict2.__setitem__('원종래', '010-9128-3434')
dict2.__setitem__('이지은', '010-2222-2222')
dict2.__setitem__('김희철', '010-3333-3333')
# 사전에 key와 value를 1:1 맵핑하여 저장할때

#name = input('검색할 이름 입력 : ')
#print(dict2.get(name))

dict2.clear()
# 사전 내의 모든 자료를 삭제

print(dict2)
keys = dict2.keys()
print(keys)
# tuple : 리스트와 유사하게 index를 통하여 접근할 수 있으나, 값의 변경 및 삭제가 불가능한 자료형

tu1 = (10,20,30,40,50)
print(tu1[0])
print(tu1[1])
print(tu1[2])
print(tu1[3])

# tu1[0] = 100    # 튜플은 멤버변수에 대입할 수 없다

li1 = [11,22,33,44,55]
print(li1[0])
li1[0] = 12         # 리스트는 멤버변수에 값을 대입할 수 있다
print(li1[0])









