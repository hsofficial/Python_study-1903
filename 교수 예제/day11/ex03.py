'''
ex03.py
'''

# 반복문 문제 1.
# 사용자에게 정수를 입력받아서, 해당 정수를 거꾸로 출력하는 코드를 작성하세요
# 입력 : 1234
# 출력 : 4321
'''
num = int(input('정수 입력 : '))   
ret = 0             # ret    num         # ret    num     # ret    num    num > 10 : False
while num > 10:     # 0      1234        # 40     123     # 430    12
    ret += num % 10 # 4      1234        # 43     123     # 432    12
    ret *= 10       # 40     1234        # 430    123     # 4320   12 
    num //= 10      # 40     123         # 430    12      # 4320   1 
ret += num
print('출력 :', ret) 


# 1을 문자열을 이용하여 while로 풀기
n1 = 1234
n1 = str(n1)
i = len(n1) - 1     # 길이값, 인덱스는 길이값과 일치할 수 없다 (0부터 세기 때문에)
while i >= 0:
    print(n1[i], end='')
    i -= 1
print()

# 1을 for으로 풀기
n1 = 12345
n1 = str(n1)
for i in range(len(n1) - 1, -1, -1):
    print(n1[i], end='')
print()

# 1.5 while을 이용하여 입력받는 모든 수를 덧셈하는 코드를 작성하세요 
# (단, 0은 덧셈에 영향을 끼치지 못하므로, 0을 입력받으면 더이상 더하지 않겠다라는 의미로 간주하고 반복을 종료)

total = 0
while True:
    num = int(input('정수 입력 : '))
    if num == 0:
        break
    total += num
    
print(total)

'''


# 반복문 문제 2.
# 길이가 2분 40초인 mp3파일이 있다. 이 파일의 재생 구간 상태를 출력하는 코드를 구현하려고한다
# 재생중인 시간을 초로 입력받아 진행률을 %로 출력하는 코드를 작성하세요
'''
mp3_len = (2 * 60) + 40
now = int(input('재생중인 시간 (초) : '))
percent = int(now / mp3_len * 100)
print('\n[', end='')
for i in range(50):     # for i in range(0,50,1)        # for(i=0;i<50;i++)
    if i == 24:
        print(' {:d}% '.format(percent), end='')
    elif i <= percent//2:
        print('#', end='')
    else:
        print(' ', end='')
print(']\n')
'''    


# 반복문 문제 3.
# 사용자에게 분 단위로 시간을 입력받아서
# mm : ss 의 형태로 남은 시간을 측정하는 타이머를 구현하는 코드를 작성하세요
from time import sleep
minute = float(input('몇 분 : '))
second = int(minute * 60)

for i in range(second, -1, -1):
    print('{:02d} : {:02d}'.format(i // 60, i % 60))
    sleep(1)    # 1초 기다리는 함수
print('\n\t[시간 다 됐어요 !!]')









