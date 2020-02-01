'''
ex03.py

문자열 인덱싱과 슬라이싱을 이용한 문제
'''

# 1. 사용자에게 문자열 형태로 숫자를 입력받아서
#    문자열의 길이가 0이하 이거나, 문자열의 길이가 3을 초과하는 경우 경고를 띄우는 코드

# 입력 : 0
# 입력 : 99
# 입력 : 1000    -> 입력된 데이터의 길이가 너무 큽니다. 3자리 이하로 입력하세요
# len(str1)
str1 = input('숫자 입력 : ')
print((len(str1) == 0) and '문자열을 입력해주세요' or 
      (len(str1) > 3) and '문자열의 길이가 너무 큽니다' or str1)


# 2. 사용자에게 E-mail 주소를 입력받고 출력하는 코드에서
#    E-mail 주소의 길이가 8자리 미만이면 경고를 출력하는 코드
#    조건을 만족한다면 @ 문자를 기준으로 왼쪽과 오른쪽을 따로 출력하기
# 입력 : admin@itbank.com
# 출력 : admin, itbank.com

# 입력 : a@b.com
# 출력 : 주소가 너무 짧습니다
mail = input('메일 주소를 입력 : ')

a, b = (len(mail) < 8) and ('주소가', ' 너무 짧습니다') or mail.split('@')

# a와 b에 값을 담는데, 길이가 8보다 작으면 각각 '주소가', '너무 짧습니다' 를 대입하고
# 길이가 8보다 작지 않으면, mail값에서 @를 기준으로 분리하여 각각 a와 b에 담는다

print((len(mail) < 8) and '{}{}'.format(a,b) or ('{}, {}'.format(a, b)))

# 값을 출력하는데 길이가 8보다 작으면 a값과 b값을 그냥 출력하고
# 길이가 8보다 작지 않으면, 문자열 서식을 지정하여 각 값을 , 로 구분하여 출력한다


# 3. 주민등록번호를 입력받아서 생년월일과 나이와 성별을 출력하는 코드를 문자열 슬라이싱으로 처리하기
# 단, 길이가 다르면 진행하지 않고 경고를 출력하기 (9305162345678)

idnum = input('주민등록번호 입력 : ')
'''
idnum = (idnum.find('-') >= 0) and idnum[:6] + idnum[7:] or idnum
idnum = (idnum.find('-') >= 0) and \
        idnum[:idnum.find('-')] + idnum[idnum.find('-')+1:] \
        or idnum        # \\n 는 줄을 바꾸지 않는다는 뜻
'''
dash = idnum.find('-')  # 찾는 문자열의 순번, 없으면 -1
idnum = (dash >= 0) and idnum[:dash] + idnum[dash+1:] or idnum
# 930516-2345678 = '930516' + '2345678' or '9305162345678' 

if len(idnum) == 13:        # 만약에, 문자열의 길이가 13이면 아래 코드를 진행한다
    year = int(idnum[:2])
    year += year > 19 and 1900 or 2000 
    month = idnum[2:4]
    date = idnum[4:6]
    age = 2019 - year + 1
    gender = (int(idnum[6]) % 2 == 0) and '여성' or '남성'
    result = '{}년 {}월 {}일 출생한 {}살 {}입니다'.format(year, month, date, age, gender)
    
else:                       # 아니면(문자열의 길이가 13이 아니면), 다음 코드를 진행한다
    result = '길이가 맞지 않습니다'

print(result)
#print((len(idnum) != 13) and '길이가 맞지 않음' or result)


