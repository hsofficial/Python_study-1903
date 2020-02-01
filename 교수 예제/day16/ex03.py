'''
ex03.py
'''

menu = -1   # 변수 선언하기 위해 초기값을 아무 값이나 넣었다
data = ['이지은', 100, 99, 87, 286, 95.33, '권지용', 99, 88, 79, 266, 88.67]

while True:
    print('1. 학생 정보 입력')
    print('2. 학생 정보 수정')
    print('3. 학생 정보 검색')
    print('4. 전체 학생 출력')
    print('0. 종료')
    print('=' * 25)
    
    menu = input('메뉴 선택 : ')    # 문자열로 입력받아서
    if menu.isdigit():          # 숫자면 정수형태로 변환
        menu = int(menu)
    else:       # 아니면 경고 메시지를 출력하고, 반복문의 시작점으로 돌아간다
        print('메뉴를 숫자로 정확히 입력하세요\n')
        continue
    
    if menu == 1: 
        data.append(input('이름 입력 : '))     # 0, 6, 12 ...
        kor = int(input('국어 입력 : '))
        data.append(kor)                    # 1, 7, 13 ...
        eng = int(input('영어 입력 : '))
        data.append(eng)                    # 2, 8, 14 ...
        mat = int(input('수학 입력 : '))
        data.append(mat)                    # 3, 9, 15 ...
        data.append(kor + eng + mat)        # 4, 10, 16 ...
        data.append(round((kor + eng + mat) / 3, 2))    # 5, 11, 17 ...
        print()
    if menu == 2: 
        flag = False
        find = input('검색할 학생의 이름 입력 : ')
        for i in range(0, len(data), 1):
            if data[i] == find:
                flag = True         # 원하는 데이터를 찾았다 !
                kor = data[i + 1]
                eng = data[i + 2]
                mat = data[i + 3]
                total = data[i + 4]
                avg = data[i + 5]
                result = '\n\t[{}] \n국어 : {}, 영어 : {}, 수학 : {}\n합계 : {}, 평균 : {:.2f}\n'
                result = result.format(data[i], kor, eng, mat, total, avg)
                print(result)
                
                name = input('변경할 이름 입력 : ')
                kor = input('변경할 국어 점수 입력 : ')
                eng = input('변경할 영어 점수 입력 : ')
                mat = input('변경할 수학 점수 입력 : ')
                
                if name != '': data[i] = name
                if kor != '': data[i + 1] = int(kor)
                if eng != '': data[i + 2] = int(eng)
                if mat != '': data[i + 3] = int(mat)
                if kor != '' and eng != '' and mat != '':
                    total = int(kor) + int(eng) + int(mat)
                    avg = round(total / 3, 2)
                    data[i + 4] = total
                    data[i + 5] = avg
                continue    # 반복문의 위로 빠져나간다 -> 코드는 위에서 아래로  움직이므로 다시 반복문에 진입
        if flag == False:
            print('[{}] : 찾을 수 없습니다'.format(find))
                
    if menu == 3: 
        flag = False    # 값을 찾지 못한 상태
        find = input('검색할 학생의 이름 입력 : ')
        for i in range(0, len(data), 1):
            if data[i] == find:
                flag = True     # 원하는 값을 찾았다 !
                kor = data[i + 1]
                eng = data[i + 2]
                mat = data[i + 3]
                total = data[i + 4]
                avg = data[i + 5]
                result = '\n\t[{}] \n국어 : {}, 영어 : {}, 수학 : {}\n합계 : {}, 평균 : {:.2f}\n'
                result = result.format(data[i], kor, eng, mat, total, avg)
                print(result)
                break
        if flag == False:       # 원하는 값을 찾지 못했다면
            print('[{}] : 찾을 수 없습니다\n'.format(find))
                
    if menu == 4: 
        for i in range(0, len(data), 1):
            if type(data[i]) == str:
                kor = data[i + 1]
                eng = data[i + 2]
                mat = data[i + 3]
                total = data[i + 4]
                avg = data[i + 5]
                result = '\t[{}] \n국어 : {}, 영어 : {}, 수학 : {}\n합계 : {}, 평균 : {:.2f}\n'
                result = result.format(data[i], kor, eng, mat, total, avg)
                print(result)
        
    if menu == 0: 
        print('프로그램을 종료합니다')
        break        
    
