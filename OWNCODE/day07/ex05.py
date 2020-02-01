'''
ex05.py

if 이용 입력값 범위 구분
'''

age = int(input('나이 입력 : '))

if age >= 90:    print('80대 이상')    #위에서부터 범위의 기준값 정하고 범위 좁혀나가는 방식
elif age >= 80:    print('80대')     #조건문의 실행문이 한줄이면 조건 + 실행문을 한줄에 이어 작성
elif age >= 70:    print('70대')
elif age >= 60:    print('60대')
elif age >= 50:    print('50대')
elif age >= 40:    print('40대')
elif age >= 30:    print('30대')
elif age >= 20:    print('20대')
elif age >= 10:    print('10대')
elif age >= 0:    print('10세 미만')
else:    print('나이는 음수값일 수 없음')
print()

#입력값의 시작값 끝값 범위 지정
#예) 사용자에게 정수 입력 (허용범위 0~100)

score = int(input('점수 입력 : '))

#if 0 <= score <= 100:        #비정상적 표현법, 될수도 아닐수도
if 0 <= score and score <= 100:
    print('점수', score)
else:
    print('점수가 허용범위를 벗어남')