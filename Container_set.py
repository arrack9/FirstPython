#C:Python31python.exe  
# -*- coding:utf-8 -*- 
'''第一行是設定直譯器所在的位置
       第二行是設定程式碼使用utf-8的編碼
   set型態'''
admins = {'Justin', 'caterpillar'} #建立set
print(admins)
users = {'momor', 'hamini', 'Justin'}
print('Justin' in admins)  # justin是否在站長群?
print(admins & users)	   # 誰同時在站長群也是使用者群?
print(admins | users)	   # 誰是站長群或是使用者群?
print(admins - users)	   # 誰是站長群但不是使用者群?
print(admins ^ users)	   # XOR
print(admins > users)      # E
print(admins < users)