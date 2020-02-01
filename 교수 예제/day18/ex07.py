'''
ex07.py

사전 자료형 가지고 놀기
'''
dict1 = {}

dict1.__setitem__('이름', ['원종래', '김희철', '이지은', '이순재'])
dict1.__setitem__('나이', [30, 36, 27, 84])
dict1.__setitem__('성별', ['남성', '남성', '여성', '남성'])

length = len(dict1.get('이름'))   # 이름이 몇명인지 구해놓기

keys = dict1.keys()     # key만 추출하여
for i in keys:          # key항목을 한줄에 출력하기
    print('\t{}'.format(i), end='')
print('\n', '=' * 40)    

for i in range(length): # 인원수만큼 반복하여
    for j in keys:      # 항목갯수만큼 
        var = dict1.get(j)[i]   # 해당항목의 인원순번째 정보를 가져옴
        print('\t{}'.format(var), end='')   # 값을 출력
    print()

