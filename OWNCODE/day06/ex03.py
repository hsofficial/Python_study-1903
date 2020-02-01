'''
ex03.py

문자열 인덱싱과 슬라이싱을 이용한 문제
'''

#1.사용자에게 문자열 형태로 숫자를 입력받아서
#  문자열의 길이가 0 이하이거나, 문자열의 길이가 3을 초과 하는 경우 경고를 띄우는 코드

str1 = input('문자열 입력:')
flag1 = (len(str1) <= 0 or len(str1) > 3)
flag1 == True and print('문자열의 길이가 너무 작거나 큼 (0이하 3초과)')  or print(str1)

#2. 사용자에게 메일주소를 입력받고 출력하는 코드에서
#   메일 주소가 8자리 미만이면 경고 출력
#   조건 만족시 @ 기준 왼쪽 오른쪽 따로 출력

mail = input('메일주소 입력:')

a, b = (len(mail) < 8) and ('주소가', '너무 짧음') or mail.split('@')
c, d = mail.split('@')

#a와 b에 값을 담는데 길이가 8보다 작으면 각각 '주소가' '너무짧음'을 대입
#길이가 8보다 작지 않으면 mail값에서 @를 기준으로 분리하여 각각 a와 b에 담음

print((len(mail) < 8) and '{} {}'.format(a,b) or ('{},{}'.format(a,b)))

#값을 출력하는데 있어서 길이가 8보다 작으면 a b 값 그냥 출력하고
#길이가 8보다 작지 않으면 문자열 서식을 지정하여 각 값을 , 로 구분하여 출력

print((len(mail) < 8) and ('{} {}'.format(c,d)) or ('{},{}'.format(a,b)))

#3. 주민등록번호를 입력받아서 생년월일 나이 성별 출력 코드 문자열 슬라이싱으로 처리
#   단 길이가 다르면 진행하지 않고 경고 출력

krid = input('주민번호 입력 :')

'''
krid = (krid.find('-') >= 0) and krid[:6] + krid[7:] or krid
krid = (krid.find('-') >= 0) and \
       krid[krid.find('-')] + krid[krid.find('-')+1] or krid
'''
dash = krid.find('-') #찾는 문자열의 순번, 없으면 1
print('dash:', dash)
krid = (dash >= 0) and krid[:dash] + krid[dash+1:] or krid
#930516-2345678 = '930516' '2345678' or '9305162345678' 

print('krid:', krid)

if len(krid) == 13:     #만약에 문자열의 길이가 13이면 아래 코드 진행
    year = int(krid[:2])
    year += (year > 19) and 1900 or 2000
    #year 값이 19보다 크면 1900 더하기 아니면 2000 더하기
    month = krid[2:4]
    date = krid[4:6]
    age = 2019 - year + 1
    gender = int(krid[6]) % 2 and '남자' or '여자'
    result = '{}년 {}월 {}일 생  {}살 {}'.format(year, month, date, age, gender)
    
else:                   #문자열 길이 13이 아니면 다음 코드 진행
    result = '길이가 서식에 맞지 않음'

print(result)

'''
print((len(krid) != 13) and '길이가 맞지 않음' or result)
'''