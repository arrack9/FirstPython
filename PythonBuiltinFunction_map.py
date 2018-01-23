#C:Python31python.exe
# -*- coding:utf-8 -*-
'''map()
   Format: map(function, sequence)
   iterate循遍所有的sequence元素並將傳入的function作用於元素，
       最後以List作為回傳值'''

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def fn(x):
    return x * 2
c = map(fn, a)
print c