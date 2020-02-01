'''
사용자에게 내용을 입력받아서, 입력받은 내용(세과목의 점수와 합계 및 평균)을
본인 컴퓨터의 바탕화면의 python_test2.txt에 저장하기
'''
file = open('C:\\Users\\user\\Desktop\\python_test2.txt', 'w')

for i in range(3):
    name = input('name : ')
    kor = int(input('국어 입력 : '))
    eng = int(input('영어 입력 : '))
    mat = int(input('수학 입력 : '))
    total = kor + eng + mat
    avg = total / 3
    result = '\t[{}]\n {}, {}, {}\n합계 : {}, 평균 : {:.2f}\n\n'
    result = result.format(name, kor, eng, mat, total, avg)
    
    file.write(result)
    
file.close()