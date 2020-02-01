'''
ex01.py

file 작성
'''

test = '%HOMEDRIVE%\%HOMEPATH%\Desktop'

'''C:\\Users\\[계정이름]\\Desktop\\[작성할파일이름]', 'w'''

f = open('C:\\Users\\user\\Desktop\\python_test.txt', 'w')
#경로를 지정하여 파일 객체를 쓰기용 / 읽기용 접근 지정
f.write('이름 : 이지은 \n')
f.write('나이 : 27 \n')
#파일 내용 작성 >>> 내용은 문자열, 변수에 내용 많이 담아서 한번에 넘기기 가능
f.close()
# 원하는 내용을 모두 작성했다면 파일 객체에게 내용 전송을 닫는다라는 신호를 보낸다