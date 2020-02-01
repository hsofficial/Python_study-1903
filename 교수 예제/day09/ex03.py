'''
ex03.py

while문 예시
'''
# 횟수에 의한 반복
cnt = 0
while cnt < 5:
    print("{}, Hello, World!".format(cnt))
    cnt += 1
    
# 횟수와 상관없이, 특정 조건에 의해서 반복되는 구문

while True:
    pw = input('itbank 라고 입력하세요 : ')
    if pw == 'itbank':
        break

while True:
    score = int(input('점수를 입력 (0 ~ 100) : '))
    if 0 <= score and score <= 100:
        break
    print('범위를 확인하고 다시 입력해주세요')    
print('점수 :', score)


# 횟수와 특정조건을 모두 설정하는 경우
# 비밀번호를 입력하는 코드, 최대 입력 시도 횟수는 3회

pw = 'kgitbank'
cnt = 3

while cnt != 0:
    password = input('비밀번호를 입력하세요 : ')
    if pw == password:
        print('로그인 성공 !!')
        break
    cnt -= 1
    print('남은 입력 시도 횟수 :', cnt)
    

# 최소 공배수 찾기
n1 = int(input('정수 입력 : '))
n2 = int(input('정수 입력 : '))

# 1. while에 조건 설정하기
a = 1
while a % n1 != 0 or a % n2 != 0:       # 반복을 실행할 조건
    a += 1

# 2. 무한 반복이후 if에 의해서 break로 탈출하기
a = 1
while True:
    a += 1
    if a % n1 == 0 and a % n2 == 0:     # 반복을 중단할 조건
        break
    
print('a :', a)



    













    
    
    
    
    
    