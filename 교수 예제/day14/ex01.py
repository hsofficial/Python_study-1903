'''
함수
    - 함수를 사용하는 이유
        1. 코드를 역할, 파트별로 나누어서 코드에 문제가 발생할 경우 유지보수를 쉽게 한다
        2. 코드의 재사용성을 높인다
        
    - 함수 사용 시의 구조
    
        def 함수이름(매개변수):
            code1
            code2
            return 반환값
            
        Func(인자)        반환값이 없는 경우 혹은 반환값을 저장하지 않는 경우
        ret = Func(인자)  반환값이 있어서, 특정 변수에 저장하는 경우
        print(Func(인자)) 반환값을 저장할 필요없이 바로 출력하는 경우

'''

def Add(n1, n2):
    return n1 + n2

Add(1,2)
3

print(Add(3,4))
print(7)

result = Add(5,6)
print(result)

word = Add('IT', 'Bank')
print(word)