'''

ex03.py
재시작 cmd 스크립트 작성

'''

path = 'C:\\Users\\user\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup'
path += '\\script.cmd'

test2 = open(path, 'w')

test2.write('start iexplore www.google.com \n') #강제로 웹사이트 실행
test2.write('shutdown /r /t 600 \n')    #강제로 종료 예약

test2.close()