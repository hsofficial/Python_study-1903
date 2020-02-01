'''
ex05.py
'''
#0. 1부터 10까지의 합 구하기
total = 0
i = 1
while i <= 10:
    total += i
    i += 1
print('total : ', total)

#1.1부터 100까지의 홀수의 합과 짝수의 합을 각각 구하여 출력
odd = 1
tot_odd = 0
while odd <= 100:
    tot_odd += odd
    odd += 2
print('total of odd numbers : ', tot_odd)

even = 2
tot_even = 0
while even <= 100:
    tot_even += even
    even += 2
print('total of even numbers : ', tot_even)
    

#2.첫날에 10원 입금, 다음날에는 이전날의 2배를 입금하는 방식으로 30일간 저축, 30일째 은행잔고
deposit = 0
money = 10
day = 1

while day <= 30:
    deposit += money    #입금 >>> 어제 준비한 돈을 오늘 은행에 입금한 직후
    money *= 2
    day += 1
    
print('deposit of', day, 'days : ', deposit)

    