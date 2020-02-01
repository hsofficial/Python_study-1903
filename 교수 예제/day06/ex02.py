'''
ex02.py
String 문자열

    문자열의 Indexing
    
word = 'itbank'

    index    [0]  [1]  [2]  [3]  [4]  [5]    첨자, 순번, 순서를 나타내는 번호
    word = [ 'i', 't', 'b', 'a', 'n', 'k' ]
'''
word = 'itbank'
print(word)
print(word[0])
print(word[1])
print(word[2])
print(word[3])
print(word[4])
print(word[5])
# print(word[6])    # out of range : 범위를 벗어났습니다

print('word의 길이 :', len(word))

# 모든 문자열은 길이값을 자동으로 가지고 있으며
# 문자열의 길이값과 일치하는 인덱스는 없다 (인덱스는 0부터 시작하기 때문에)
# 문자열의 마지막 값을 구하는 방법은 인덱스에 (길이 - 1)을 넣으면 된다

test = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
print(test[0])
print(test[1])
print(test[2])
print(test[3])
print(test[len(test) - 1])
print(test[-1])

# 문자열의 Slicing : 인덱스의 시작지점과 끝지점을 지정하여 문자열의 일부를 잘라내는 기법
# word[시작점:끝점] (끝점의 내용은 포함하지 않습니다)

print(test[0:4])    # 4번째의 E를 포함하지 않고 출력한다
print(test[4])
print(test[:4])     # 시작점 생략 0:4
print(test[-4:])    # 끝점생략 -4:끝글자    (len(test) - 1)

# 예제) 주어진 문자열에서 일부만 추출하여 출력해보세요
# 슬라이싱을 할때에도 음수의 인덱스를 사용할 수 있다
# 슬라이싱에서 시작점을 생략하면 첫글자로 간주하고, 끝점을 생략하면 마지막글자로 간주한다
str1 = "20190325Monday"

# 1. 날짜의 연도만 출력하기
print(str1[0:4])
print(str1[:4],'년', sep='')
print(str1[:4] + '년')
# print(1 + 2)

# 2. 날짜의 월과 일을 구분하여 출력하기 (xx월 xx일)
print(str1[4:6], str1[6:8])
print(str1[4:6], '월', str1[6:8], '일')
print(str1[4:6] + '월 ' + str1[6:8] + '일')
print(int(str1[4:6]), '월 ' + str1[6:8] + '일')
print('{}월 {}일'.format(str1[4:6], str1[6:8]))

# 1과 2를 합치면
print('{}-{}-{}'.format(str1[:4], str1[4:6], str1[6:8]))

# 3. 요일을 출력하기
print(str1[-6:])    # 끝에서 6글자만큼만 출력하자



idnum = '9305162345678'
A = (int(idnum[:2]) > 19) and int(idnum[:2]) + 1900 or int(idnum[:2]) + 2000
B = idnum[2:4]
C = idnum[4:6]
D = int(idnum[6]) % 2 and '남성' or '여성'
# 모든 정수값은 참과 거짓을 표현할 수 있으며, 0은 False, 0이 아닌 모든 값은 True로 판단

result = '{}년 {}월 {}일 {}'.format(A, B, C, D)

print(result)

print(0 and True or False)
print(1 and True or False)      # Non-Zero : 0이 아닌 모든 숫자값
print(100 and True or False)
print(-100 and True or False)

print('Hello, world!')




















