'''
ex03.py

대입 연산자

    기본 대입 연산자의 기능과 처리 순서 : =
    복합 대입 연산자와 배정 대입 연산자 : += -= *= /= //= %= (산술연산 대입연산 결합)

'''
a = 1           #변수에 상수값 대입
b = 1 + 2       #우변에 연산자 있으면 연산 수행 이후 최종값 변수에 대입
c = a + b       #우변에 변수 있으면 변수 값 대입
d = a + 1       #변수와 상수를 연산식에 섞어서 사용 가능
word = 'hello'  #문자열도 상수로 취급
                #우변을 먼저 처리하고 최종값이 나온 후에야 대입을 한다
a = a + 1       # a+1값 먼저 계산하고 계산되어 나온 값을 다시 변수에 대입
a = 'example'   #어떤 변수의 자료형이 정수였더라도, 다른 자료형을 대입하면 값이 바뀐다(자료형도 바뀐다)
pi = round(3.141592653589, 3)   #함수(기능) y=f(x)

print('a :', a)
print('b :', b)
print('c :', c)
print('d :', d)
print('word :', word)
print('pi :', pi)

#a = a + 1 >>> a += 1

a = 10
print('a :', a)

a += 1          #복합 대입은 기존의 값에 산술연산 결과 대입 (값 유지되면서 증가 OR 감소)
print('a :', a)

a = 1           #일반 대입은 기존 값 덮어씌움 (값 삭제)
print('a :', a)

a -= 2
print('a :', a)

a *= 3
print('a :', a)

num = 1234
total = 0
tmp = num % 10
num //= 10      #num = num // 10
total += tmp
print('num :', num, 'tmp :', tmp, 'total :', total)

#복합대입연산의 예시
total = 0
total += int(input('과목 1 점수 입력  :'))
total += int(input('과목 2 점수 입력  :'))
total += int(input('과목 3 점수 입력  :'))
avg = round(total / 3, 2)
print('합계 :', total, '평균 :', avg)

# = 은 대입연산, == 은 크기비교연산
if total == 300: print('만점자입니다')