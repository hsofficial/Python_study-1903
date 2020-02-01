'''
ex03.py

대입 연산자

    . 기본 대입 연산자의 기능, 처리 순서 : =
    . 복합 대입 연산자, 배정 대입 연산자 : +=, -=, *=, /=, //=, %= (산술연산과 대입연산의 결합)

'''
a = 1           # 변수에 상수값을 대입할 수 있다
b = 1 + 2       # 우변에 연산자가 있으면, 연산을 수행한 이후 최종값을 변수에 대입
c = a + b       # 우변에 변수가 있으면, 변수의 값을 대입
d = a + 1       # 변수와 상수를 연산식에 섞어서 사용 가능
word = 'Hello'  # 문자열도 상수로 취급
                # 우변을 먼저 처리하고, 최종값이 나온 후에야 대입을 한다
a = a + 1       # a + 1의 값을 먼저 계산하고, 계산되어 나온 값을 다시 a변수에 대입한다
a = 'itbank'    # 어떤 변수의 자료형이 정수였더라도, 다른 자료형을 대입하면 값이 바뀐다(자료형도 바뀐다)
pi = round(3.1415926535, 3)     # 함수(기능)    y = f(x)

print('a :', a)
print('b :', b)
print('c :', c)
print('d :', d)
print('word :', word)
print('pi :', pi)

# a = a + 1  ->  a += 1

a = 10
print('a :', a)
a += 1          # 복합대입은 기존의 값에 산술연산한 결과를 대입 (값이 유지되면서 증가하거나 감소하거나)
print('a :', a)
a = 1           # 일반 대입은 기존의 값을 덮어씌운다. (값이 유지되지 않는다)
print('a :', a)

a -= 2
print('a :', a)

a *= 3
print('a :', a)


# 복합대입연산의 예시
num = 1234
total = 0
tmp = num % 10
num //= 10      # num = num // 10
total += tmp
print('num :', num, ', tmp :', tmp, ', total :', total)


# 복합대입연산의 예시
total = 0
total += int(input('첫번째 점수 입력 : '))
total += int(input('두번째 점수 입력 : '))
total += int(input('세번째 점수 입력 : '))
avg = round(total / 3, 2)
print('합계 :', total, ', 평균 :', avg)

#  = : 대입연산
# == : 크기비교연산

if total == 300:    print('만점')
























