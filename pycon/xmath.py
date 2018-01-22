#C:Python31python.exe  
# -*- coding:utf-8 -*- 
'''
Created on 2018�~1��18��

@author: Pingyao.Chen
'''
def max(a, b):
    return a if a > b else b
def min(a, b):
    return a if a < b else b

def suma(*numbers): # numbers 接受可變長度引數
    total = 0
    for number in numbers:
        total += number
    return total

pi = 3.141592653589793
e = 2.718281828459045