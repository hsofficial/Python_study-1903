'''
ex04.py

split() 함수 연습
'''

#사용자의 주민번호를 입력 형식은 XXXXXX-XXXXXXX
#입력 후 앞 6자리와 뒤 7자리 별도 변수 저장
#정수로 변환하여 각 값 출력

KR_id = input('주민등록번호 입력 : ')
birth,personal = KR_id.split('-') #문자열에서 구분자를 찾아서(-) 구분자 기준 오른쪽 왼쪽 값 준비

birth = int(birth)
personal = int(personal)
#birth, personal = '930516', '2222222'

print('{:d} - {:d}'.format(birth, personal))

#birth 이용 >> 년 월 일 나이 구하기 (year 4자리 년도 구하기)

date = birth % 100  #9305.[16]
birth //= 100       #[9305].16
month = birth % 100 #93.[05]
year = birth // 100 #[93].05
year += (year > 19) and 1900 or 2000
age = 2019 - year + 1

#personal 이용 >> 성별 식별

gender  = ((personal // 1000000) % 2 != 0) and '남자' or '여자'
#           [2].345678

#서식 포함 문자열 결과 출력

result = "{}년 {}월 {}일 출생한  {}세  {}입니다".format(year, month, date, age, gender)
print(result)