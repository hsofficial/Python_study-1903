'''
ex02.py

print()에서 서식 활용, Escape Sequence 활용
    특수문자
    \n : 다음줄로 커서이동 (nl, LF)
    \t : 탭 크기만큼 커서를 우측으로 이동 (4칸 혹은 8칸)
    \r : 현재 줄의 가장 왼쪽(줄의 처음)으로 커서 이동 (CR)
    \b : 현재 위치에서 왼쪽으로 한칸 커서 이동
    \a : 경고음 발생

'''

print('hello\nworld')
print('hello\tworld')
print('hello\rworld')
print('hello\bworld')
print('hello\aworld')

print
print('원빈  \t: 42')
print('이순재 \t: 82')
print('유노윤호 \t: 37')
print('크리스티나 : 40')

print('hello', 'itbank')
print('hello', 'itbank', end = '\n', sep=' ')
#print 함수는 기본적으로 값과 값사이를 띄워쓰기로 구분(sep), 출력이 끝나면 마지막에 \n(end)출력

var1 = 'python'
var2 = 'you'
var3 = 'need'
print(var2, end=' ')    #end 값 미지정시 한줄 내리도록 설정
print(var3, end=' ')    #사용자가 직접 값 지정
print(var1, end=' ')    #줄을 바꾸지 않거나 띄워쓰기 하도록 변경 가능
print()

print(var2, var3, var1)
print(var2, var3, var1, sep='_')    #separtor(구분자)

#서식 (format)

name = '김설현'
age = 26
score = 95.33333333333333333

#문자열 서식
print('{}님의 나이는 {}살 입니다'.format(name, age))         #string,decimal(10진수)
print('{:s}님의 나이는 {:d}살 입니다'.format(name, age))
print('{:10s}님의 나이는 {:5d}살 입니다'.format(name, age))
print('{:>10s}님의 나이는 {:>5d}살 입니다'.format(name, age))
print('{:<10s}님의 나이는 {:<5d}살 입니다'.format(name, age))
print('{:^10s}님의 나이는 {:^5d}살 입니다'.format(name, age))
print('{:-^10s}님의 나이는 {:^5d}살 입니다'.format(name, age))
print('{:*^10s}님의 나이는 {:^5d}살 입니다'.format(name, age))
print('{:#^10s}님의 나이는 {:^5d}살 입니다'.format(name, age))
print('\n\t{:=^50s}\n'.format('절취선'))

#실수 서식
print('점수는 {}점 입니다'.format(score))
print('점수는 {:f}점 입니다'.format(score))    #float(실수)
print('점수는 {:.2f}점 입니다'.format(score))  #소수점 둘째자리까지 출력
print('점수는 {:.0f}점 입니다'.format(score))  #정수인것처럼 소수점 이하 자리 출력하지 않음
print(score)        #원래의 값 그대로 유지 (출력시에만 서식 지정)

#정수 서식 1 >>> 시간 출력
hour = 14
tmin = 2
sec = 9
print('지금 시간은 {:02d} : {:02d} : {:02d} 입니다'.format(hour, tmin, sec))

#정수 서식 2. 천단위 구분기호 출력하기
cost = 2000000
print('제품의 가격은 {}원'.format(cost))
print('제품의 가격은 {:,d}원'.format(cost))

print('나이는 %d살' % 12)   #C언어 문법 >>>printf("나이는%d살\n", 12);
print('점수는 %.2f점' % score)
#C언어문법 >>>printf("가격은 %,d원\n", cost); (XXXXXXXX)
