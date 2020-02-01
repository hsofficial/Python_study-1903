'''
ex01.py

기본 if문제
'''

# 1. 세 수를 입력받아서 가장 작은 수를 출력하세요

A = int(input('정수 입력 : '))
B = int(input('정수 입력 : '))
C = int(input('정수 입력 : '))

if A < B:   minimum = A
else:       minimum = B

if minimum > C: minimum = C

print('{}, {}, {}중 최소값은 {}이다\n'.format(A, B, C, minimum))

# 2. 세 수를 입력받아서 가장 큰 수를 출력하세요

n1 = int(input('정수 입력 : '))
n2 = int(input('정수 입력 : '))
n3 = int(input('정수 입력 : '))

if n1 > n2: big = n1
else:       big = n2

if big < n3:    big = n3

print('{}, {}, {}중 최대값은 {}이다\n'.format(n1, n2, n3, big))



# 3. 입력받은 수의 절대값을 출력하세요

num = int(input('정수 입력 : '))
if num < 0: num = -num
print('절대값 :', num)











'''
# 4. 두 수를 입력받아서, 두 수의 최소공배수를 구하세요
n1 = int(input('n1 : '))
n2 = int(input('n2 : '))

result = n1 * n2
small, big = (n1 < n2) and (n1, n2) or (n2, n1)

if n1 % 2 == 0 and n2 % 2 == 0 and (result // 2) % n1 == 0 and (result // 2) % n2 == 0:
    result //= 2

elif big % small == 0:
    result //= small
    

print(result)
'''   
     
