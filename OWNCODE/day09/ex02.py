'''
ex02.py
반복문(loop) 코드의 특정 부분을 조건에 따라서(while) 혹은 지정 횟수에 의해(for) 반복
    
    while : 조건에 따라서 반복하기 때문에 코드의 형태는 if와  유사하게 진행
        *단 if는 조건이 참이면 한번 진행
        *while은 조건이 참이면 무한정 반복(매번 조건을 확인하므로 조건이 변경되면 무한은 아니다)
'''
num = 10

if num < 20:
    print('ifnum',num)
    num += 1
    
while num < 20:
    print('whilenum',num)
    num += 1
    
print('mainnum', num)

'''
while True:
    print('infinite loop')
'''

from time import sleep
coin = 1
while True:
    print('동전이 {:,d}개'.format(coin))
    coin *=2
    sleep(1)
    if coin > 10000:
        break   #반복문 중단