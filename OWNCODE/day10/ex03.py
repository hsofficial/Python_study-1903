'''
ex03
'''

#1에서 100사이 수 중에서 3과 5의 공배수인 수만 출력
#3으로도 나누어 떨어지고 5로도 나누어 떨어지는 수

data = int(input('정수 입력'))

for i in range (1, data+1): # 밤위 지정 >>> 범위중 특정 숫자가 i
    chk = True              # 소수 판별 check 논리연산 >>> false 인지 아닌지 검사
    if i % 3 != 0 or i % 5 != 0:
        chk = False         # chk에 False을 저장(자기자신을 제외하고 나누어 떨어지면 조건 탈락)
        
    if chk == True:         # chk 값이 False가 아니면 3과 5의 공배수 이므로 출력
        print(i, end=" ")
print()

#중첩 for 문 이용한 19단 출력

for i in range(2,20):
    print(i, '단')
    for j in range(1,20):
        print('{} x {} = {}'.format(i, j, i * j))
    print()
    
for i in range(5):
    for j in range(5):
        print('# ', end='')
    print()
print()

for i in range(5):
    for j in range(5):
        if i == j:
            print('# ', end='')
        else:
            print('  ', end='')
    print()
print()

for i in range(5):
    for j in range(5):
        if i == 2 or j == 2:
            print('# ', end='')
        else:
            print('  ', end='')
    print()
print()

for i in range(5):
    for j in range(5):
        if i % 2 == 1 or j % 2 == 1:
            print('# ', end='')
        else:
            print('  ', end='')
    print()
print()

cnt = 0
for i in range(5):
    for j in range(5):
        cnt += 1
        print('{:2d}'.format(cnt), end='')
    print()
print()