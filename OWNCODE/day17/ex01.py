'''
ex01.py

리스트를 이용하여 순위 매기기

모두 1등에서 시작하고 나보다 높은 사람이 발견되면 나의 등수를 1 증가시킨다
'''

name = ['강동원', '유인나', '하정우', '이순재', '김새론']
score = [99,77,88,95,79]
rank = [1,1,1,1,1]

for i in range(0, len(score)):      #비교 기준의 범위(처음~끝)
    for j in range(0, len(score)):  #비교 대상의 범위(처음~끝)        
        if score[i] < score[j]:     #기준점수가 대상점수보다 작으면
            rank[i] += 1            #기준등수 1 증가
print()   
print('이름', name)
print('점수', score)
print('등수', rank)
print()

for i in range(5):
    var1 = name[i]
    var2 = score[i]
    var3 = rank[i]
    result = '[{}] {}점, {}등'.format(var1, var2, var3)
    print(result)
print()

# 등수 매긴 이후에 등수를 기준으로 리스트를 정렬하기(오름차순)

for i in range(0, len(rank)):
    for j in range(i, len(rank)):
        if rank[i] > rank[j]:
            
            tmp = rank[i]
            rank[i] = rank[j]
            rank[j] = tmp
            
            tmp = name[i]
            name[i] = name[j]
            name[j] = tmp
            
            tmp = score[i]
            score[i] = score[j]
            score[j] = tmp

for i in range(5):
    var1 = name[i]
    var2 = score[i]
    var3 = rank[i]
    result = '[{}] {}점, {}등'.format(var1, var2, var3)
    print(result)
print()