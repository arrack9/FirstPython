#C:Python31python.exe  
# -*- coding:utf-8 -*-
'''
python code判斷None的主要3個方式
1. If x is None:
2. If not x:
3. If not x is None:(這樣理解更清晰if not (x is None))
'''
xx = 1
print not xx
yy = [1]    #list 
print not yy
zz = 0
print not zz
jj = [0]    #list
print not jj
print jj 

'''
在python中 None, False空字符串"",0,空list[],空dict{},空tuple()都當於False
<strong>not None == not False == not '' == not 0 == not [] == not {} == not()</strong>
'''
