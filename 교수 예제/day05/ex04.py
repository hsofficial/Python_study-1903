'''
ex04.py

split() 함수 연습해보기
'''

# 사용자의 주민등록번호(가상)을 입력받고, 형식은 xxxxxx-xxxxxxx 의 형식으로 한다
# 입력받은 후 앞 6자리와 뒤 7자리를 별도의 변수에 저장하고
# 정수로 변환하여 각 값을 출력하세요

idnum = input('주민등록번호를 입력 (xxxxxx-xxxxxxx) : ')
num1 = 0
num2 = 0

num1, num2 = idnum.split('-')   # 문자열에서 -를 찾아서, -를 기준으로 왼쪽과 오른쪽 값을 준비한다

# num1, num2 = '930516', '2222222'

num1 = int(num1)    # num1 = 930516
num2 = int(num2)    # num2 = 2222222

print('{:d}-{:d}'.format(num1, num2))

# num1을 이용하여 year, month, date, age를 구하고 (year는 4자리 연도로 구하세요)
# num2를 이용하여 gender를 구한 후
# 서식을 포함하는 문자열 result를 완성하세요

print(result)










