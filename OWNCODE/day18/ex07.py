'''
dict 자료형
'''

dict1 = {}
dict1.__setitem__('이름', ['이지금', '이지은','이지동','이지철'])
dict1.__setitem__('나이', [25, 26, 27, 28])
dict1.__setitem__('성별', ['여성', '여성', '여성', '남성'])

length = len(dict1.get('이름'))             # 이름이 몇명인지

keys = dict1.keys()                         # key만 추출
for i in keys:                              # key항목을 한줄에 출력
    print('\t{}'.format(i), end='')
print('\n', '=' * 40)    

for i in range(length):                     # 인원수만큼 반복
    for j in keys:                          # 항목갯수만큼 
        var = dict1.get(j)[i]               # 해당항목의 인원순번째 정보를 가져옴
        print('\t{}'.format(var), end='')   # 값을 출력
    print()