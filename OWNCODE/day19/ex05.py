'''
ex05.py

여러 학생의 점수를 관리할 수 있는 프로그램을 작성하고 (리스트)
파일 입출력을 활용하여, 저장하기 및 불러오기 기능을 추가하세요
메뉴를 구성하고, 각 기능은 함수로 처리
'''
# 시작하기 전에 먼저 함수를 정의한다
from os import system       # cmd에서 사용하는 명령어를 직접 전달하기 위한 파이썬 모듈
from time import sleep
from codecs import open     # (텍스트) 파일을 불러오기 하면서 인코딩 방법도 지정할 수 있는 함수


def InputData():    #학생 1인의 데이터룰 하나의 파일로 관리 - 완료
    tmp = []        # [0] 이름, [1] 국어, [2] 영어, [3] 수학, [4] 합계, [5] 평균
    tmp.append(input('이름 입력 : '))
    kor = int(input('국어 입력 : '))
    eng = int(input('영어 입력 : '))
    mat = int(input('수학 입력 : '))
    print()
    total = kor + eng + mat
    avg = total / 3
    tmp.append(kor)
    tmp.append(eng)
    tmp.append(mat)
    tmp.append(total)
    tmp.append(avg)
    return tmp

def FindData(data): #데이터 검색기 - 완료
        find = input('검색할 학생의 이름 입력 : ')
        flag = True
        for i in range(len(data)):
            if data[i][0] == find:
                flag = False
                name = data[i][0]
                kor = data[i][1]
                eng = data[i][2]
                mat = data[i][3]
                total = data[i][4]
                avg = data[i][5]
                result = '\n\t[{}] \n국어 : {}, 영어 : {}, 수학 : {}\n합계 : {}, 평균 : {:.2f}\n'
                result = result.format(name, kor, eng, mat, total, avg)
                print(result)
                return i    # data 리스트에서 몇번째 위치에 있는지를 반환
        if flag:
            print('[{}] : 찾을 수 없습니다'.format(find)) 
            return -1   # data 리스트에서 원하는 데이터가 없으면 -1을 반환하기로 규칙을 설정

def DeleteData():   #pop(인덱스) - 인덱스에 위치한 값을 리턴하면서 삭제 - 완료
    find = input('삭제하고자 하는 학생의 이름 입력 : ')
    for i in range(len(data)):
        if data[i][0] == find:
            data.pop(i)
            print('[Successfully removed data record.]')
            break
    print()

def ViewAll(data):  #전체 레코드 출력 - 완료
    print()
    for i in range(len(data)):
        name = data[i][0]
        kor = data[i][1]
        eng = data[i][2]
        mat = data[i][3]
        total = data[i][4]
        avg = data[i][5]
        result = '[{}] 합계 : {}, 평균 : {:.2f}\n 국어 : {}, 영어 : {}, 수학 : {}\n'
        result = result.format(name, total, avg, kor, eng, mat )
        print(result)
    print()

def SaveFile(data):
    filename = input('파일이름을 지정하세요 : ')
    f = open(filename, 'w', encoding='utf8')
    save = ''
    for i in range(len(data)):
        for j in range(len(data[i])):
            save += str(data[i][j])
            save += ':' # 각각의 데이터를 구분하는 구분자
        save += '\r\n'    # 각 줄을 구분하는 구분자
    save += ';'         # 파일의 종료를 알리는 기호
    
    f.write(save)
    f.close()
    print('[Successfully saved data.]')
    system('start notepad ' + filename)
    # start 는 새로운 프로세스로 프로그램을 실행하는 윈도우 명령
    sleep(2.5)
    # sleep(초) 지정된 초 만큼 지연(delay)시키는 기능
    system('taskkill /F /IM notepad.exe | findstr a')
    # taskkill 작업관리자에서 지정된 프로세스를 종료시키는 명령어
    
'''
def SaveData_txt(): #데이터 txt 저장 - 완료
    print('# 자료는 바탕화면에 [savefile.txt]로 저장됩니다.')
    print('# 이름, 국어점수, 영어점수, 수학점수, 총점, 평균 순으로 저장됩니다')
    print('# 주의 : 바탕화면에 동일 명칭의 파일이 있으면 덮어쓰기 합니다')
    print()
    
    f = open('C:\\Users\\user\\Desktop\\savefile.txt', 'w')
    print('Preview of savefile.txt')
    print('=' * 50)
    
    for i in range(len(data)):
        name = data[i][0]
        kor = data[i][1]
        eng = data[i][2]
        mat = data[i][3]
        total = data[i][4]
        avg = data[i][5]
        result = '{}, {}, {:.2f}, {}, {}, {} \n'
        result = result.format(name, total, avg, kor, eng, mat )
        print(result)
        f.write(result)
    f.close()
    
    print('=' * 50)
    print('[Successfully saved data.]')
    print()
''' 
def LoadFile():
    filename = input('불러올 파일 이름을 입력 : ')
    dir1 = system('dir | findstr ' + filename)
    print(dir1)
    if dir1 == 0:
        f = open(filename, 'r', encoding='utf8')
        #f = open(filename, 'r')
        result = f.read()               #파일 불러오기
        list1 = result.split('\r\n')    #줄별 구분 리스트1 생성
        result = []                     #result는 결과를 반환하기 위한 빈 리스트로 새로 생성
        for i in range(len(list1)):
            if list1[i] != ';':     # 파일의 마지막이 아니면
                tmp = list1[i].split(':')   # 각 줄을 :으로 구분한 tmp리스트를 만들어낸다
                tmp2 = []
                for j in range(len(tmp)):
                    if tmp[j].find('.') >= 0:
                        tmp2.append(float(tmp[j]))
                    elif tmp[j].isnumeric():
                        tmp2.append(int(tmp[j]))
                    elif tmp[j] == '':
                        pass
                    else:
                        tmp2.append(tmp[j])
                result.append(tmp2)
        return(result)
    return []
'''
def ImportData_txt(): #txt 파일에서 data import
    print('*자료는 바탕화면에 [savefile.txt]로 저장되야 합니다.')
    print('*자료의 저장 형식은\n이름, 합계, 평균, 국어, 영어, 수학\n꼴이어야 합니다\n')
    f = open('C:\\Users\\user\\Desktop\\savefile.txt', 'r')
    result = f.read()
    result = result.split(', ')
    print(result)
'''
    
        
data = [
        ['이지은', 100, 99, 87, 286, 95.33], 
        ['홍진호', 22, 22, 22, 66, 22.00],
        ['김희철', 99, 88, 79, 99+88+79, (99+88+79) / 3]
    ]

#Splash Interface

while True:
    print('* 성적 데이터 관리 시스템 *')
    print('=' * 50)
    print('1. 학생 데이터 입력')
    print('2. 학생 데이터 검색')
    print('3. 학생 데이터 삭제')
    print('4. 학생 데이터 전체 조회')
    print('5. 데이터를 txt 파일로 저장하기')
    print('6. txt 파일에서 데이터 불러오기')
    print('0. 종료')
    print('=' * 50)
    menu = input('메뉴 선택 >>> ')
    print()
    
    if menu == '1': data.append(InputData())
    if menu == '2': FindData(data)
    if menu == '3': DeleteData()
    if menu == '4': ViewAll(data)
    if menu == '5': SaveFile(data)
    if menu == '6': data = LoadFile()
    if menu == '0':
        print('[Exit the program. Unsaved data will be deleted]')
        break