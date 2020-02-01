'''
ex03.py

'''

#1.나이 입력받아 성인과 미성년자 판별

age=int(input("나이 입력  : "))

print(age >= 20 and "성인" or "미성년자")
#[조건]and[TRUE]or[FALSE] >>>삼항 연산자

#2.후불카드 잔액과 결제 금액 통하여 결제 성공/실패 여부 판단

card = 5000
pay = int(input('결제금액  : '))
print(pay <= card) #조건 TF 판단

print(pay <= card and '결제완료' or '결제실패')
#결제금액이 카드 잔액보다 작거나 같으면 성공
print('카드잔액', pay <= card and str(card - pay) or card, '원' )
#결제금액이 카드잔액보다 작거나 같으면 금액 차감
#1과 0으로 논리 결정
#값이 0이면 F 판단

#3 Q)사용자에게 문자열 입력 > itbank 성공 아니면 실패
print('itbank')
word = input('위 글자를 그대로 입력하시오 : ')
print(word == 'itbank' and '성공' or '실패') #같다

#4. 음료수의 구매 개수 입력받아 음료수의 개수가 3으로 나누어 떨어지면 1개의 값을 차감하여 출력 >>> 2+1

drink_price = 800
count = int(input('구매 개수 : '))

print('총 가격은', count % 3 >= 0 #조건:개수가 3개 이상
      and (drink_price * (count - count // 3)) #개수가 3으로 나누어 떨어지는 만큼 개수를 1개 차감
      or drink_price * count) #아니면 제값 받기