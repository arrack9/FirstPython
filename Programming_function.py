#C:Python31python.exe  
# -*- coding:utf-8 -*- 
'''�i�H�ϥΨ禡�ӫʸ˵{�����q�A�N�y�{���ޥΤ��P�ƭȩ��ܼƪ������]�p���Ѽ�'''
def max(a, b):
    return a if a > b else b
print(max(3, 9))
def power(x):
	return x ** 3
print(power(9))

'''�bPython���A�i�H�ϥ�lambda��ܨөw�q�@�Ө禡'''
a = 1
b = 99
min = lambda a, b: a if a < b else b
minium = min
print(min(10, 20))
print(minium(1, 99))