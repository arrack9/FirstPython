#C:Python31python.exe  
# -*- coding:utf-8 -*- 
from sys import argv
if len(argv) > 1:
   print 'Hello, ' + argv[1]
else:
   print 'Hello, Guest'

a = 12
b = 7
if a > b:
   print(a)
else:
   print(b)
'''�p�W�d�Ҥ]�i�H�g���p�U'''
print 'Hello, ' + (argv[1] if len(argv) > 1 else 'Guest')   
print a if a > b else b
