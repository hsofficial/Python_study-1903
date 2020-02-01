'''
ex01.py
'''

from time import sleep
from os import system

second = int(input('타이머 시간입력 (초) : '))

for i in range(second, -1, -1):
    system("cls")
    print('\n\t{:02d} : {:02d}'.format(i // 60, i % 60))
    sleep(1)

print("End !")
