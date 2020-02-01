'''
ex03.py
'''

#q1)사용자에게 정수를 입력받아 해당 정수를 거꾸로 출력하는 코드

num = str(input('정수 입력 :'))
i = len(num) - 1    #길이값, 인덱스는 길이값과 일치할 수 없다


while i >= 0:
    print(num[i], end='')
    i -= 1
print()

'''
n1 = 12345
n1 = str(n1) - 1
for i in range(len(n1) - 1, -1, -1):
    print(n1[i], end='')
    print()
'''

#q1.5)while 이용 입력받는 모든 수 덧셈 코드 / 0을 입력받으면 반복 종료
num2 = 0

while True:
    num1 = int(input('더할 수 입력 : '))
    if num1 == 0:
        break
    num2 += num1
print(num2)

#q2) 길이 2분 40초 음악 / 파일의 재생 구간 상태 출력 코드 / 시간 초로 입력받아 진행률 % 출력
playtime = int(input('재생 시간 초로 입력:'))
playpersent = (playtime / 160) * 100
print('\n[',end='')
for i in range(50):
    if i == 24:
        print(' {}% '.format(playpersent),end = '')
    elif i <= playpersent // 2:
        print('=',end='')
    else:
        print('', end='')
print(']\n')

#q3) 사용자에게 분단위 시간 입력 / mm:ss 형태로 남은시간 측정 타이머

from time import sleep
num_min = float(input('분단위로 시간 입력 :'))
num_sec = int(num_min * 60)

for i in range(num_sec, -1, -1):
    print('{:02d}:{:02d}'.format(num_sec// 60, num_sec % 60))
sleep(1)
print('\n\t[시간 지남]')
    
'''
long == len(num)

while(long > 0):    long -= 1

print(num[long], end=' ')
print()
'''