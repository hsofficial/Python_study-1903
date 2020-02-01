'''
ex05.py
'''
# 0. 1부터 10 사이의 합을 구하기

total = 0
i = 1
while i <= 10:
    total += i
    i += 1
print('합계 :', total) 

# 1. 1부터 100사이의 홀수의 합과 짝수의 합을 각각 구하여 출력하세요

odd_sum = 0
even_sum = 0

i = 1
while i <= 100:
    if i % 2 == 0: even_sum += i
    else:           odd_sum += i
    i += 1
print('홀수의 합 : {}, 짝수의 합 : {}'.format(odd_sum, even_sum))




# 2. 첫날에 10원을 입금하고, 다음 날에는 이전날의 두배를 입금하는 방식으로 30일간 저축할 경우
#    30일 째의 은행 잔고를 구하세요

money = 10
day = 1
bank = 0

while day <= 30:
    bank += money   # 입금    <- 어제 준비한 돈을 오늘 은행에 입금한 직후
    if day <= 30:   # 연산자를 == 로 하면 30일차때의 결과만 출력, <= 30일 이하 모든 결과를 출력
        print('{}일차때의 은행 잔고는 {:,d}'.format(day, bank))
    money *= 2      # 다음날을 위해서 돈을 2배 준비함
    day += 1        # day 증가
    












