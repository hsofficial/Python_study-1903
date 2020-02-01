'''
ex03.py
'''

menu = -1   #변수 선언 위해 초기값 임의 지정
data = ['이지은',100,100,100,300,100, '아이유',99,99,99,297,99]

while True:
    print('1. 학생 정보 입력')
    print('2. 학생 정보 수정')
    print('3. 학생 정보 검색')
    print('4. 전체 학생 출력')
    print('0. 프로그램 종료')
    print('=' * 25)
    
    menu = input('메뉴 선택 : ')    #문자열로 입력
    
    if menu.isdigit():              #숫자면 정수형태로 변환
        menu = int(menu)
        
    else:                           #아니면 경고 메시지 출력 >>> 반복문 시작점으로 돌아감
        print('메뉴를 숫자로 정확히 입력하세요\n')
        continue
    
    if menu == 1:
        data.append(input('이름 입력'))
        
        kr = int(input('국어 입력'))
        data.append(kr)
        
        en = int(input('영어 입력'))
        data.append(en)
        
        ma = int(input('수학 입력'))
        data.append(ma)
        
        data.append(kr + en + ma)
        data.append(round((kr + en + ma) / 3 , 2))
        print()
        
    if menu == 2:
        flag = False
        find = input('검색할 학생의 이름 입력 : ')
        for i in range(0, len(data), 1):
            if data[i] == find:
                flag = True
                kr = data[i + 1]
                en = data[i + 2]
                ma = data[i + 3]
                total = data[i + 4]
                avg = data[i + 5]
                result = '\n\t[{}] \n국어 : {}, 영어 : {}, 수학 : {}\n합계 : {}, 평균 : {:.2f}\n'
                result = result.format(data[i], kr, en, ma, total, avg)
                print(result)
                
                name = input('변경할 이름 입력 : ')
                kr = input('변경할 국어 점수 입력 : ')
                en = input('변경할 영어 점수 입력 : ')
                ma = input('변경할 수학 점수 입력 : ')
                
                
                
                if name != '' : data[i] = name
                if kr != '' : data[i + 1] = int(kr)
                if en != '' : data[i + 2] = int(en)
                if ma != '' : data[i + 3] = int(ma)
                if kr != '' and en != '' and ma != '':
                    total = int(kr) + int(en) + int(ma)
                    total = int(total)
                    avg = round(total / 3, 2)
                    data[i + 4] = total
                    data[i + 5] = avg
                continue
                # 반복문의 위로 빠져나간다 -> 코드는 위에서 아래로  움직이므로 다시 반복문에 진입
        if flag == False:
            print('[{}] : 찾을 수 없음'.format(find))
        
    if menu == 3:
        flag = False
        find = input('검색할 학생의 이름 입력 : ')
        for i in range(0, len(data),1):
            if data[i] == find:
                flag = True
                kr = data[i + 1]
                en = data[i + 2]
                ma = data[i + 3]
                total = data[i + 4]
                avg = data[i + 5]
                result = '\n\t [{}] \n korean : {}, English : {}, Math : {} \n Total : {}, Average : {:.2f} \n'
                result = result.format(data[i], kr, en, ma, total, avg)
                print(result)
                break
        if flag == False:
            print('[{}] : 찾을 수 없습니다\n'.format(find))
        
    if menu == 4:
        for i in range(0, len(data), 1):
            if type(data[i]) == str:
                kr = data[i + 1]
                en = data[i + 2]
                ma = data[i + 3]
                total = data[i + 4]
                avg = data[i + 5]
                result = '\n\t[{}] \n국어 : {}, 영어 : {}, 수학 : {}\n합계 : {}, 평균 : {:.2f}\n'
                result = result.format(data[i], kr, en, ma, total, avg)
                print(result)
                
    if menu == 0: 
        print('프로그램을 종료합니다')
        break        