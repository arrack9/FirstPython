#C:Python31python.exe  
# -*- coding:utf-8 -*-
'''__builtin__中的reduce,有時在別的語言中會被稱為foldLeft，
       它其實代表了高度抽象化的流程重用，只要是打算從清單中求值都可使用'''
reduce(lambda calsum, elem: calsum + elem, [1, 2, 3, 4, 5], 0)   

# reduce(add, [1,2,3,4,5],0)