#C:Python31poython.exe
# -*- coding:utf-8 -*-
filename = input('檔名:')

rfile = open(filename, 'r', encoding='UTF-8')
content = rfile.read()
rfile.close()

print(content)
print(content.encode('UTF-8'))
print(content.encode('UTF-8').decode('UTF-8'))
