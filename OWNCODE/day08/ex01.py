'''
ex01.py

if 문제
'''

#1. 사용자에게 국영수 점수 입력받고 합계 평균 구하기
#점수에 따라서 평점 a+abcdef 출력
#100/a+ ~90/a ~80/b ~70/c ~60/d 60~/f

krscore = int(input('국어 점수 입력 :'))
enscore = int(input('영어 점수 입력 :'))
mascore = int(input('수학 점수 입력 :'))
print()

scsum = krscore + enscore + mascore
scavg = round(scsum / 3 , 2)
gpa = ''

if scavg > 100:
    print('입력값 범위 초과')
elif scavg == 100:
    gpa = 'A+'    #위에서부터 범위의 기준값 정하고 범위 좁혀나가는 방식
elif scavg >= 90:
    gpa = 'A'
elif scavg >= 80:
    gpa = 'B'
elif scavg >= 70:
    gpa = 'C'
elif scavg >= 60:
    gpa = 'D'
else:
    gpa = 'F'
    
print('점수 합계는 {}, 평균은 {}, 학점은 {}'.format(scsum,scavg,gpa))