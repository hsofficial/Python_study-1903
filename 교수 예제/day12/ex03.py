'''
ex03.py
'''

# 1. 사용자가 0을 입력할 때 까지 점수를 입력받아 합계를 구하고 평균을 출력하는 코드를 작성하세요
# (사용자가 1 ~ 100 사이의 범위를 벗어나는 점수를 입력하면 합계에 반영하지 않는다)

i = 0
total = 0

while True:
    score = int(input('점수 입력 : '))
    
    if 0 < score and score <= 100:  # case 1
        i += 1
        total += score
    elif score == 0:                # case 2
        print('{}개 과목의 결과\n합계 : {}, 평균 : {:.2f}'.format(i, total, total / i))
        break
    else:                           # case 3
        print('점수가 범위를 벗어났습니다')
    




