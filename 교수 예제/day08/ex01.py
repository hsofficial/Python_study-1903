'''
ex01.py

if 문제
'''

# 1. 사용자에게 국어, 영어, 수학 점수를 입력받고 합계와 평균을 구하여
#    점수에 따라서 평점 [A+, A, B, C, D, F]로 구분하여 출력하세요

#    avg    100    ~90    ~80    ~70    ~60    60~
#    grade   A+     A       B      C      D      F

kor = int(input('국어 점수 입력 : '))
eng = int(input('영어 점수 입력 : '))
mat = int(input('수학 점수 입력 : '))

total = kor + eng + mat
avg = total / 3

if avg > 100:   
    print('점수 입력이 잘못되었습니다')
    grade = ''  # 값을 지정하지는 않고, 변수공간만 미리 만들어두기 위해서 사용한다
    total = 0
    avg = 0
    
elif avg == 100:  grade = 'A+'
elif avg >= 90: grade = 'A'
elif avg >= 80: grade = 'B'
elif avg >= 70: grade = 'C'
elif avg >= 60: grade = 'D'
elif avg < 60: grade = 'F'

print('합계 : {}, 평균 : {:.2f}, 평점 : {}'.format(total, avg, grade))














