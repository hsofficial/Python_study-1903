'''
ex02.py

논리 연산자
'''

# 1. 놀이기구의 탑승조건에 따라서 연령과 키를 입력받고, 탑승 여부를 출력하는 코드 작성
#     키 : 150cm 이상, 연령 : 10살 이상

height = float(input('키 : '))
age = int(input('나이 : '))

cond = (height >= 150) and (age >= 10)
print(cond and '탑승 가능합니다' or '탑승 불가입니다')

# 2. 5과목의 성적을 입력받아, 평균을 구하고 합격 / 불합격 여부를 출력하는 코드
#    평균이 60점 이상이고, 각 과목은 40점 미만이 없어야 합격
#     
sub1 = int(input('1과목 점수 입력 : '))
sub2 = int(input('2과목 점수 입력 : '))
sub3 = int(input('3과목 점수 입력 : '))
sub4 = int(input('4과목 점수 입력 : '))
sub5 = int(input('5과목 점수 입력 : '))
total = sub1 + sub2 + sub3 + sub4 + sub5 
avg = total / 5
avg = round(avg, 3)

cond1 = not sub1 < 40 and sub2 >= 40 and sub3 >= 40 and sub4 >= 40 and sub5 >= 40
cond2 = avg >= 60
cond3 = cond1 and cond2
print()
print('총점 :', total,', 평균 :', avg)
print(cond3 and '합격' or 
      (not cond1) and '불합격(과락)' or '불합격(평균부족)')
      

  













