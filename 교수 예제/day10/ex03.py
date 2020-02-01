'''
ex03.py

'''

# 1에서 100 사이의 수 중에서 3과 5의 공배수인 수만 출력하세요
# (3으로도 나누어 떨어지는 동시에 5로도 나누어 떨어지는 수만 출력하기)

for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
        print(i, end=' ')
print()


for i in range(1,101):
    flag = True
    if i % 3 != 0 or i % 5 != 0:
        flag = False
    
    if flag:
        print(i, end=' ')
print()
        
# 중첩된 for문을 이용한 구구단 출력하기

for dan in range(2,10):   # 2 ~ 9
    print(dan,'단')
    for mul in range(1,10):   # 1 ~ 9
        print('{} x {} = {}'.format(dan, mul, dan * mul))
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
        print('{:2d}'.format(cnt), end=' ')
    print()     
print()        
 
        
        
        
        
        
        
        
        
        
        
        
        
        