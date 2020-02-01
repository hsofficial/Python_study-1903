'''
quiz02.py

사용자에게 이름, 키 , 체중 입력
    표준체중 = (키 - 100)*0.9 (kg)
    비만도=(현재 체중/ 표준체중) * 100 (%)
출력

'''

name = input("name")
length = float(input('키 입력(cm) :'))
weight = int(input("무게 입력(kg) :"))

standard_weight = (length - 100) * 0.9
bmi = (round((weight / standard_weight) * 100 , 3))
#round(3.141592,3) 소수점 셋쩨자리에서 반올림

print()
print(name, '님의 표준 체중은 :',standard_weight, '(kg)')
print(name, '님의 비만도는' ,bmi, '(%)')
