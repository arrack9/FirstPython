#C:Python31python.exe
# -*- coding:utf-8 -*-
'''lambda
Python提供了一個簡易的function define: lambda,
用完即丟，不著痕跡
其中的expression這一行指令不能放等號(=)
lambda運算式(expression)有一個參數(parameter)，運算結果回傳冒號後的運算式
'''
from _ast import Expression
lambda param1, param2: Expression

def func(param1, param2):
    return Expression

func = lambda x,y,z : x+y+z

def func2(x, y, z):
    return x + y +z

my_list = [1, 2, 3]
map(lambda i: i * i, my_list)

print(func(1,2,3))
print func2(1,2,3)
print map(lambda i: i + i, my_list)


f = lambda x: x ** x
print(f(1))
print(f(2))
print(f(3))
print(f(4))
print(f(5))

'''
array[], dict{}, tuple()
'''
nlist = ()
calsum = lambda nlist: nlist+100

