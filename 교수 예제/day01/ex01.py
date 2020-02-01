'''
Ctrl + s : 저장
Ctrl + F11 : 실행
'''
print("hello")
print()

def fib(n):
    a,b = 0, 1
    while a < n:
        print(a, end=' ')
        a,b = b, a+b
    print()
    
fib(1000)
