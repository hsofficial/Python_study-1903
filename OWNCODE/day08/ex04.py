'''
ex04.py
question
'''
#1. 사격 연습 게임을 만들려고 한다. 사격용 권총의 유효거리는 50~150m 사이이다.
#사용자와 목표의 거리를 입력받아서 1)적정유효거리 2) 유효거리보다멀다 3)유효거리보다 가깝다

user_name = str(input('사용자 성명 : '))
target = int(input('목표 거리 입력  : '))

if target > 150:
    trange = '유효거리 초과'
elif target >= 50 and target <= 150:
    trange = '적정 유효거리 '   #위에서부터 범위의 기준값 정하고 범위 좁혀나가는 방식
elif target < 50:
    trange = '유효거리 미만'
else:
    trange = '입력오류'

print(user_name, '님의 목표거리는', trange)
print()

#2. 놀이공원에 말을 타는 코너가 있다. 이용시간에 따라 요금을 지불, 기본료 3000(30분).
#10분당 500원 추가 이용료 발생. 시간>>>요금 코드 작성

usetime = int(input('사용 시간 입력 : '))

if usetime < 30:
    fare = 3000
else:
    fare = 3000 + ( ( (usetime // 10) - 3) * 500 )

print('요금은', fare, '원')
print('요금 : {:,d}'.format(fare))
print()

#.15층 건물에 엘리베이터 3대 / ABC 중 가장 가까운 엘리베이터 한대만 이동
#사용자 호출 층수 입력>>> 엘리베이터 출력 코드 작성4
#a=5 b=3 c=13

cfloor = int(input('현재 층수 입력 : '))

A, B, C = 5, 3, 13

distanceA = cfloor - A
distanceB = cfloor - B
distanceC = cfloor - C

if distanceA < 0:    distanceA *= -1
if distanceB < 0:    distanceB *= -1
if distanceC < 0:    distanceC *= -1

if distanceA > distanceB :    result = distanceC
else:    result = distanceB    
if distanceA <= result :    distanceA

if result == distanceA:    print('A이동')
elif result == distanceB:    print('B이동')
else:    print('C 이동')
