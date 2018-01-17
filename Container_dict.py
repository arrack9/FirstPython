#C:Python31python.exe  
# -*- coding:utf-8 -*- 
'''第一行是設定直譯器所在的位置
       第二行是設定程式碼使用utf-8的編碼
   dict型態'''
passwords = {'Justin': 123456, 'caterpillar': 933933, 'Pingyao': 696969}
print(passwords['Pingyao'])
passwords['Mochi'] = 799977   #增加一對鍵值
print(passwords)
del passwords['Pingyao']      #刪除一對鍵值
print(passwords)
print(passwords.items())
print(passwords.keys())
print(passwords.values())

''' 使用 [] 時如果指定的鍵不存在，會發生 KeyError，
          可以使用 dict 的 get 方法，指定鍵不存在時傳回的預設值。例如： '''
print(passwords.get('openhome', '000000'))
print(passwords.get('Justin', '2222222'))


