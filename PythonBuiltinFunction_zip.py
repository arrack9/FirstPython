#C:Python31python.exe  
# -*- coding:utf-8 -*-
'''
Python的__builtin__模組中有一些函式，不需要import也可以使用
zip
'''   
keynumbers = [12, 35, 13, 12]
brand = ['ASUS', 'HP', 'DELL', 'ACER'] 
print {number : name for number, name in zip(keynumbers, brand)}