'''
ex01.py

함수(function)

    1. 변수 : 데이터를 저장하는 공간
    2. 연산자 : 데이터와 데이터 간의 계산, 연산, 처리를 담당하는 기호
    3. 함수 : 변수와 연산자를 활용하여 일정한 처리를 하나의 기능으로 묶어둔 코드의 집합
    
'''

n1 = 1
n2 = 2

print('{}+{}={}'.format(n1,n2,n1+n2) )
print('{}+{}={}'.format(2,4,2+4) )
print('{}+{}={}'.format(3,6,3+6) )
print('{}+{}={}'.format(4,8,4+8) )
print()

#위의 print()로 출력되는 결과를 똑같이 출력하면서, print를 한번만 사용 (반복문)

for i in range(0,5,1):
    a = i + 1
    b = (i + 1) * 2
    print('{}+{}={}'.format(a,b,a+b) )
print()

for i in range(4):
    a = i + 1
    b = (i + 1) * 2
    print('{}+{}={}'.format(a,b,a+b) )
print()

#두 수의 합을 출력하는 코드의 예시

def Add(a, b):
   print('{}+{}={}'.format(a,b,a+b) ) 
   
for i in range(0,5,1):
    a = i + 1
    b = (i + 1) * 2
    Add(a, b)
Add(64, 128)
Add(32768, 65536)

#y = f(x)

'''
 
n1 = 1
n2 = 2
n3 = n1 + n2

while True:
    print('{}+{}={}'.format(n1,n2,n1+n2) )
    n1 += 1
    n2 += 2
    
'''