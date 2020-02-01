'''
quiz02.py

사용자에게 이름, 키 , 체중 입력
    표준체중 = (키 - 100)*0.9 (kg)
    비만도=(현재 체중/ 표준체중) * 100 (%)
출력

'''

'''입력'''
name = input("이름 입력 : ")
length = float(input('키 입력(cm) :'))
weight = float(input("무게 입력(kg) :"))

'''계산'''
standard_weight = round((length - 100) * 0.9 , 3) # 표준체중
bmi = (round((weight / standard_weight) * 100 , 3)) # 비만도
# cf) round(3.141592,3) 소수점 셋째자리에서 반올림
# bmi = round(bmi,3) 꼴 도 가능함

'''출력'''
print()
print(name, '님의 표준 체중은 :',standard_weight, '(kg)')
print(name, '님의 비만도는' ,bmi, '(%)')
