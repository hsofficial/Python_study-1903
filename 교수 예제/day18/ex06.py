'''
학번과 이름을 사전자료형에 대입하기
'''

stu = {}

stu.__setitem__('20190001', '원종래')
stu.__setitem__('20190002', '이지은')
stu.__setitem__('20190003', '김희철')

print(stu)
print(stu['20190001'])  # 사전자료형은 리스트의 index대신 key를 사용하는 자료형이다
print(stu.get('20190002'))
print(stu.get('2019003'))   # key가 일치하지 않으면, None을 반환한다

# index    [0]       [1]     [2]        # index는 정수자료형만 오면서, 0부터 시작
# list = ['원종래', '이지은', '김희철']

# key  =  '0001'   '0002'  '0003'       # key는 아무 자료형이나 순서가 상관없다
# dict = ['원종래', '이지은', '김희철']

keys = stu.keys()

print('모든 key를 가져와서 모든 value를 출력하기')
for i in keys:      # keys에 있는 각각의 값을 i라고 할때
    print(stu.get(i))   # 각 key를 stu.get()에 넣어서 모든 값을 출력하겠다
    
values = stu.values()
print('모든 value를 바로 출력하겠다')
for i in values:    # values의 각각의 값을 i라고 할때
    print(i)        # i를 출력해라
    









