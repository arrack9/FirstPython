#C:Python31python.exe  
# -*- coding:utf-8 -*-
'''
Python��__builtin__�Ҳդ����@�Ǩ禡�A���ݭnimport�]�i�H�ϥ�
zip
'''   
keynumbers = [12, 35, 13, 12]
brand = ['ASUS', 'HP', 'DELL', 'ACER'] 
print {number : name for number, name in zip(keynumbers, brand)}