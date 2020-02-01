'''
ex04.py

문제 풀기
'''

# 1. 사격 연습 게임을 만들려고 한다. 사격용 권총의 유효 사거리는 50m ~ 150m 사이이다
#    사용자와 목표의 거리를 입력받아서, 1) 적정 유효 거리, 2) 유효 거리보다 멀다, 3) 유효 거리보다 가깝다
#    를 출력하는 코드를 작성하세요

dist = int(input('목표로부터의 거리를 입력하세요 : '))
if dist < 50:   print('너무 가깝습니다')
elif dist > 150:print('너무 멀리 있습니다')
else:           print('유효 사정거리입니다')


# 2. 놀이공원에 말을 타는 코너가 있다. 이용 시간에 따라 요금을 지불하는데
#    기본 요금은 3000원이고, 10분 마다 500원의 추가 이용요금이 발생한다
#
#    시간     ~30     ~40     ~50     ~60    ...
#    요금    3000    3500    4000    4500    ...
#
#     시간을 입력받아 요금을 출력하는 코드를 작성하세요

time = int(input('말을 탄 시간 : '))  # 시간을 입력
base = 3000                       # 기본요금은 3000원이다
overtime = time - 30              # 추가시간은 시간 - 30(분)

# 시간이 30보다 작으면 기본요금
# 아니면 추가요금 계산(수식)
'''
if time < 30 : fee = 3000
else:          fee = ((time - 21) // 10) * 500 + base
print('요금 : {:,d}원'.format(fee)) 
'''
if time < 30: fee = 3000            # 기본요금
elif time % 10 == 0: fee = ((overtime // 10)) * 500 + base   # 10분단위이면 +1 하지 않음
else: fee = ((overtime // 10) + 1) * 500 + base              # 그 외에는 +1 적용한다
print('요금 : {:,d}원'.format(fee))


# 3. 15층 건물에 엘리베이터가 3대 있다. A, B, C 엘리베이터 중에서 가장 가까운 엘리베이터 한대만 이동하는
#    알고리즘을 구현하려고 한다. 사용자가 호출한 층수를 입력받아서 어떤 엘리베이터가 이동하는지 출력하는 코드를
#    작성하세요 (A = 5, B = 3, C = 13)

call = int(input('현재 위치를 입력하세요 : '))

A ,B, C = 5, 11, 13

distA = call - A        # 호출지점과의 거리값을 구하기 위해서 (차이를 구하기 위해서 뺄셈)
distB = call - B
distC = call - C

if distA < 0: distA *= -1       # 거리값이 만약 음수로 나온다면, 양수로 바꿔라
if distB < 0: distB *= -1
if distC < 0: distC *= -1       # 세 거리값 중에서 가장 작은 값을 찾아라

if distB >= distC: result = distC    # B와 C를 비교해서 더 작은 값을 result에 담고
else:             result = distB    
if distA <= result:result = distA   # A와 result를 비교해서 A가 더 작으면 result를 A로 교체한다

if result == distA : print('A가 이동합니다')      # 최소 거리값이 각 거리값과 비교해서 같은 엘베가 이동
elif result == distB : print('B가 이동합니다')
else : print('C가 이동합니다') 























