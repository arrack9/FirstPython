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
print('%d %.3f %s' % (1, 99.2, 'Justin'))
'''字串替換---舊式寫法'''
print('%(real)s is %(nick)s' % {'real':'Justin', 'nick':'caterpillar'})
print('%(osx)s is %(Mac System)s' % {'osx':'win7', 'Mac System':'Windows System'})
'''字串替換---format寫法'''
print'{0} is {1}'.format('Justin', 'caterpillar')
print'{real} is {nick}'.format(real = 'Justin', nick = 'caterpillar')
print'{0} is {nick}'.format('Justin', nick = 'caterpillar')
import sys
print('My platform is {pc.platform}'.format(pc = sys))

