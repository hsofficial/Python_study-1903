'''
ex01.py
'''

from time import sleep
from os import system

second = int(input('시간 입력(초):'))

for i in range(second, -1, -1):
    system("cls")
    print('{:02d}:{:02d}'.format(i // 60, i % 60))
    sleep(1)
    
print('end')