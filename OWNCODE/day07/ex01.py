'''
ex01.py
'''

#1. 지하철을 타고 이동할 때 총 이동 구간수가 10정거장 미만이면 구간당 2분으로 계산
#   총 이동 구간 수가 10정거장 이상이면 구간당 3분으로 계산
#   입력>>>이동시간, 출력>>>총 소요시간
#   (단 시간이 60분 초과하는 경우 x시간 x분 형식 출력 미만일 경우 분으로 출력)

sublen = input('이동 구간 수를 입력하시오 : ')
sublen = int(sublen)

if sublen < 10 :
    time = 2
    
else :
    time = 3
    
esttime = sublen * time

result = esttime <= 60 and '예상 소요시간은 {}분'.format(esttime) \
        or '예상 소요시간은 {}시간 {}분'.format(esttime // 60, esttime % 60)
        #총시간 // 60 = hour, 총시간 % 60 = min

print(result)
    