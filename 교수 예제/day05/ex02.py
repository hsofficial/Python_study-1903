'''
ex02.py

print()에서 서식 활용하기, Escape Sequence 활용하기

    특수 문자
    
    \n : 다음 줄로 커서를 이동한다 (nl, LF)
    \t : 탭 크기만큼 커서를 우측으로 이동한다(4칸 혹은 8칸)
    \r : 현재줄의 가장 왼쪽(줄의 처음)으로 커서를 이동한다 (CR)
    \b : 현재 위치에서 왼쪽으로 한칸 커서를 이동한다
    \a : 경고음을 발생시킨다
    
'''
print('1. Hello\nPython')
print('2. Hello\tPython')
print('3. Hello\rPython')
print('4. Hello\bPython')
print('5. Hello\aPython')
print()

print('원빈 \t: 42')
print('이순재 \t: 82')
print('유노윤호 \t: 37')
print('크리스티나 : 25')
print()

print('Hello', 'ITBANK')
print('Hello', 'ITBANK', end='\n', sep=' ')
# print()함수는 기본적으로 값과 값 사이를 띄워쓰기로 구분하며(sep), 출력이 끝나면 마지막에 \n(end)을 출력한다

var1 = 'Python'
var2 = 'You'
var3 = 'need'

print(var2, end=' ')    # end 값을 지정하지 않으면 한줄 내리도록 설정되어 있으나
print(var3, end=' ')    # 사용자가 직접 값을 지정하여
print(var1, end=' ')    # 줄을 바꾸지 않거나, 띄워쓰기를 하도록 변경할 수 있다
print()

print(var2, var3, var1)
print(var2, var3, var1, sep='_')    # separtor (구분자)
print()

# 서식 (format)
name = '김설현'
age = 26
score = 95.333333333
# 문자열 서식
print('{}님의 나이는 {}살입니다'.format(name, age))
print('{:s}님의 나이는 {:d}살입니다'.format(name, age))  # String, Decimal(10진수)
print('{:10s}님의 나이는 {:5d}살입니다'.format(name, age))
print('{:>10s}님의 나이는 {:>5d}살입니다'.format(name, age))
print('{:<10s}님의 나이는 {:<5d}살입니다'.format(name, age))
print('{:^10s}님의 나이는 {:^5d}살입니다'.format(name, age))
print('{:-^10s}님의 나이는 {:^5d}살입니다'.format(name, age))
print('{:*^10s}님의 나이는 {:^5d}살입니다'.format(name, age))
print('{:#^10s}님의 나이는 {:^5d}살입니다'.format(name, age))
print('\n\t{:=^50s}\n'.format(' 절취선 '))

# 실수 서식
print('점수는 {}점입니다'.format(score))
print('점수는 {:f}점입니다'.format(score)) # Float (실수)
print('점수는 {:.2f}점입니다'.format(score))   # 소수점 둘째자리까지 출력
print('점수는 {:.0f}점입니다'.format(score))   # 정수인것처럼 소수점 이하자리 출력하지 않음
print(score)            # 원래의 값은 그대로 유지된다 (출력시에만 서식을 지정)
print()

# 정수 서식 1. 시간 출력하기
hour = 14
min = 2
sec = 9
print('지금 시간은 {:02d} : {:02d} : {:02d} 입니다'.format(hour, min, sec))

# 정수 서식 2. 천 단위 구분 기호 출력하기

cost = 2000000
print('제품의 가격은 {} 원 입니다'.format(cost))
print('제품의 가격은 {:,d} 원 입니다'.format(cost))   # <- 문자열.format(변수, 상수) 

print('나이는 %d살입니다' % 12)        # printf("나이는 %d살입니다\n", 12);
print('점수는 %.2f점입니다' % score)   
print('가격은 %,d원입니다' % cost)     # printf("가격은 %,d원입니다\n", cost); (X)































