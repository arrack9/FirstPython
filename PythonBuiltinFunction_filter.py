#C:Python31python.exe
# -*- coding:utf-8 -*-
'''filter()
   Format: filter(function, sequence)
       以傳入boolean function作為函式，
   iterate所有的sequence元素並收集function為True的元素到一個list'''

def fn(x):
    return x if x > 5 else None
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
b = filter(fn, a)
print b