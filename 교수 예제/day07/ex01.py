'''
ex01.py
'''

# 1. 지하철을 타고 이동할 때 총 이동 구간 수가 10정거장 미만이면 구간당 2분으로 계산하고
#    총 이동 구간 수가 10정거장 이상이면 구간당 3분으로 계산하기로 한다
#    이동 구간 수를 입력받아서 총 소요시간을 출력하는 코드를 작성하세요
#    (단, 시간이 60분을 초과하는 경우에는 x시간 x분 의 형식으로 출력하고, 미만인 경우는 분만 출력하기)

# 입력
distance = int(input('이동 구간 수 : '))

# 처리
time = distance < 10 and 2 or 3 
e_time = distance * time
result = e_time <= 60 and "{}분입니다".format(e_time) \
         or "{}시간 {}분입니다".format(e_time // 60, e_time % 60) 
            # 총 시간 // 60 = hour, 총 시간 % 60 = minute
 
# 출력
print(result)



