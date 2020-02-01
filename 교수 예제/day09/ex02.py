'''
ex02.py

반복문 (loop) : 코드의 특정 부분을 조건에 따라서(while), 혹은 지정된 횟수에 의해(for) 반복하는 구문

    while : 조건에 따라서 반복하기 때문에, 코드의 형태는 if와 유사하게 진행된다
            . 단 if는 조건이 참이면 한번 진행하지만
            . while은 조건이 참이면 무한정 반복한다(매번 조건을 확인하므로 조건이 변경되면 무한은 아니다)
'''

num = 10

if num < 20:
    print('if) num :', num)
    num += 1
    
while num < 20:
    print('while) num :', num)
    num += 1

print('main) num :', num)

'''
while True:
    print('무한 반복 !!')
'''
from time import sleep
coin = 1
while True:
    print('동전이 {:,d}개 있습니다'.format(coin))
    coin *= 2
    sleep(1)
    if coin > 10000:
        break       # 반복문의 중단(반복문의 아래로 탈출)










