#C:Python31python.exe
# -*- coding:utf-8 -*-
str = "Just'in"
print(str)
str1 = 'Just"in'
print(str1)
str2 = 'c:\workspace'
print(str2)
str3 = "c:\\workspace"
print(str3)
str4 = 'c:\todo'
print(str4)
str5 = r'c:\todo'
print(str5)
str6 = "c:\\todo"
print(str6)
name = "Pingyao"
for ch in name:
    print(ch)
print(len(name))
print('P' in name)
print((name+' ')*3)
lang = 'python'
print(lang[0])
print(lang[-2])
print(lang[0:])
print(lang[2:3])
print(lang[:6])
'''每隔5個字元取值'''
print(lang[0:6:5]) 
'''字串反轉'''
print(lang[::-1]) 