'''
ex02.py

for문 이용하여 도형 만들기
'''

star = '☆'
space = '   '

for i in range(5):
    print(star * (i + 1))
    
for i in range(5):
    print(space * (i + 1), end='')
    print(star * (4 - i))
print()
# 마름모 도형 만들기
length = 5
st = 1
sp = length // 2 
for i in range(length):
    print('  ' * sp, end='')  # space 2번
    print('* ' * st, end='')  # * + space 1번
    print('  ' * sp, end='')  # space 2번
    print()
    if i < length // 2:
        st += 2
        sp -= 1
    else:
        st -= 2
        sp += 1
print()


# 모래시계 모양 만들기
length = 5
st = length
sp = 0 
for i in range(length):
    print('  ' * sp, end='')  # space 2번
    print('* ' * st, end='')  # * + space 1번
    print('  ' * sp, end='')  # space 2번
    print()
    if i < length // 2:
        st -= 2
        sp += 1
    else:
        st += 2
        sp -= 1
print()











# 나비 모양 만들기

length = 5
st = 1
sp = length - st * 2 
for i in range(length):
    if i == length // 2:
        print('* ' * length)
    else:
        print('* ' * st, end='')  # * + space 1번
        print('  ' * sp, end='')  # space 2번
        print('* ' * st, end='')  # * + space 1번
        print()
    
    if i < length // 2:
        st += 1
        sp -= 2
    else:
        st -= 1
        sp += 2
print()








 
 
 