#C:Python31python.exe  
# -*- coding:utf-8 -*- 
'''ㄏノㄧΑㄓ杆祘Α琿盢瑈祘いまノぃ计┪跑计场砞璸把计'''
def max(a, b):
    return a if a > b else b
print(max(3, 9))
def power(x):
	return x ** 3
print(power(9))

'''Pythonいㄏノlambdaボㄓ﹚竡ㄧΑ'''
a = 1
b = 99
min = lambda a, b: a if a < b else b
minium = min
print(min(10, 20))
print(minium(1, 99))