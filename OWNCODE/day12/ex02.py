'''
ex02.py
for문 이용하여 도형 만들기
'''
star = '⭐'
space = '   '

for i in range(5):
    print(star * (i + 1) )

for i in range(5):
    print(space * (i + 1), end='')
    print(star * (4 - i) )

length = 5
st = 1
sp = length // 2
   
for i in range(length):
    print("  " * sp, end='')
    print("* "  * st, end='')
    print("  " * sp, end='')
    print()
    
    if i < length//2:
        st += 2
        sp -= 1
    else:
        st -= 2
        sp += 1
        
print()

length = 5
st = length
sp = (length // 2) - 2

for i in range(length):
    print("  " * sp, end='')
    print("* "  * st, end='')
    print("  " * sp, end='')
    print()
    
    if i < length // 2:
        st -= 2
        sp += 1
    else:
        st += 2
        sp -= 1
print()

length = 5
st = length
sp = (length // 2) - 2

for i in range(length):
    print("  " * sp, end='')
    print("* "  * st, end='')
    print("  " * sp, end='')
    print()
    
    if i < length // 2:
        st -= 2
        sp += 1
    else:
        st += 2
        sp -= 1
print()