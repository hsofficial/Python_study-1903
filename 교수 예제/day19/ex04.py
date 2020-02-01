'''
ex04.py

파일 읽기
'''
from time import sleep

f = open('C:\\windows\\system32\\drivers\\etc\\hosts', 'r')

result = f.read()
result = result.split('\n')

for i in range(len(result)):
    print(result[i])
    sleep(1)
