#C:Python31python.exe  
# -*- coding:utf-8 -*-
'''__builtin__中的reduce,有時在別的語言中會被稱為foldLeft，
       它其實代表了高度抽象化的流程重用，只要是打算從清單中求值都可使用'''
sssum = 0
nlist = []
def Totalsum(nlist):
    global sssum
    for n in nlist:
        sssum += n
    return sssum
        
print Totalsum([1, 2, 3, 4, 5])

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
def fn(x, y):
    return x+y
d = reduce(fn, a)
print d