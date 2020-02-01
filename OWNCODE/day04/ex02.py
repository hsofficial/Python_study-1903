'''
ex02.py

논리 연산자
'''

#1. 놀이기구의 탑승조건에 따라서 연령과 키를 입력받고 탑승 여부 출력
#    키 : 150cm 이상, 연령: 10살 이상

height = float(input('키  : '))
age = int(input('나이 : '))

cond = (height >= 150) and (age >= 10)
print(cond and '탑승가능' or '탑승불가')
print()

#2. 5과목의 성적을 입력받아 평균을 구하고 합불 여부 출력
#    평균 60점 이상, 각 과목 40점 미만 없어야 합격

score1 = int(input('과목 1의 점수 입력 :'))
sub_cond1 = not(score1 < 40)
print('과목 1 통과 여부 :', sub_cond1 and '통과' or '과락')
print()

score2 = int(input('과목 2의 점수 입력 :'))
sub_cond2 = not(score2 < 40)
print('과목 2 통과 여부 :', sub_cond2 and '통과' or '과락')
print()

score3 = int(input('과목 3의 점수 입력 :'))
sub_cond3 = not(score3 < 40)
print('과목 3 통과 여부 :', sub_cond3 and '통과' or '과락')
print()

score4 = int(input('과목 4의 점수 입력 :'))
sub_cond4 = not(score4 < 40)
print('과목 4 통과 여부 :', sub_cond4 and '통과' or '과락')
print()

score5 = int(input('과목 5의 점수 입력 :'))
sub_cond5 = not(score5 < 40)
print('과목 5 통과 여부 :', sub_cond5 and '통과' or '과락')
print()

all_score = score1 + score2 + score3 + score4 + score5
average_score = (all_score) / 5

'''
대체 코드
pass_status = (average_score >= 60) and (score1 >= 40) and (score2 >= 40) and (score3 >= 40) and (score4 >= 40) and (score5 >= 40)
'''

pass_status = (average_score >= 60) and sub_cond1 and sub_cond2 and sub_cond3 and sub_cond4 and sub_cond5

'''
대체 코드
print('평균은 :', average_score,'>>>합격여부 :', pass_status and '합격' or '불합격')
print('평균은 합격조건을', average_score >= 60 and '충족함' or '충족하지 못함')
'''

print('총점은 :', all_score)
print('평균은 :', average_score,'>>>합격여부 :', pass_status and '합격' or
      ( (average_score >= 60) and '불합격(평균은 만족하나 과락 과목 있음)' or '불합격(평균 기준 미달)') )