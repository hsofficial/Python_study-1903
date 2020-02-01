'''
ex03.py
'''

#사용자가 0을 입력할때 까지 점수를 입력받아 합계를 구하고 평균을 출력하는 코드를 작성
#사용자가 1-100 범위 벗어나는 점수를 입력하면 합계에 반영하지 아니함
scoresum = 0
counter = 0

while True:
    num1 = int(input('더할 점수 입력 : '))
    
    if num1>= 1 and num1 <= 100:
        scoresum += num1
        counter += 1
        
    elif num1 == 0:
        counter += 0
        break
    
    else:
        print('범위 벗어남')
    
avgscore = int(scoresum / counter)

print()
print('합계는 {}점, {}개 과목의 평균은 {:.2f}점'.format(scoresum,counter,avgscore))