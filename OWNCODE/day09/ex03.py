'''
ex03.py

while문 예시
'''
#횟수 의한 반복
cnt = 0
while cnt < 5:
    print("{}, hello".format(cnt))
    cnt +=1
    
#횟수와 상관없이 특정 조건에 의해서 반복
while True:
    pw = input('input "itbank" ')
    if pw == 'itbank':
        break
while True:
    score = int(input('점수 입력(0~100)'))
    if 0<= score and score <= 100:
        break
    print('범위 오류  재입력 요망')
print('점수 : ', score)

#횟수와 특정조건 모두 설정하는 경우
#비밀번호 입력 최대 입력 횟수 3회

pw = 'kgitbank'
cnt = 3

while cnt != 0:
    password = input('비밀번호 입력')
    if pw == password:
        print('login ok')
        break
    cnt -= 1
    print('잔여 시도 횟수', cnt)
    
#최소공배수 찾기
n1 = int(input('정수입력'))
n2 = int(input('정수입력'))

#*while에 조건 설정
a = 1
while a% n1 != 0 or a % n2 != 0:
    a += 1

#* 무한 반복 이후 if에 의해서 break 탈출
a =1
while True:
    a += 1
    if a % n1 == 0 and a % n2 ==0:
        break
    
print('a : ',a)