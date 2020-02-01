'''
ex05.py

if를 이용하여 입력값의 범위를 구분하기
'''

age = int(input('나이를 입력하세요 : '))

if age >= 90:      print('80대 이상')    # 위에서 부터 범위의 기준값을 정하고
elif age >= 80:    print('80대')        # 범위를 점점 좁혀나가는 방식
elif age >= 70:    print('70대')        # 조건문의 실행문이 한줄이면 조건 + 실행문을 한줄에 이어서 작성
elif age >= 60:    print('60대')
elif age >= 50:    print('50대')
elif age >= 40:    print('40대')
elif age >= 30:    print('30대')
elif age >= 20:    print('20대')
elif age >= 10:    print('10대')
elif age >= 0:     print('10세 미만')
else:              print('나이는 음수값일 수 없습니다')
print()


# 입력값의 시작값과 끝값의 범위를 지정하기
# 예) 사용자에게 점수를 입력받으세요 (허용범위는 0 ~ 100 사이입니다)

score = int(input('점수 입력 : '))

# if 0 <= score <= 100:        # 되는 경우도 있으나, 정상적인 표현법은 아니다

if 0 <= score and score <= 100:
    print('점수 :', score)
else:
    print('점수가 허용범위를 벗어났습니다')










