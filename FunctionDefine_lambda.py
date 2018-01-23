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
list[], dict{}, tuple()
'''

alist = []
blist = [1,2,3,4]
bdict = {}
ddict = {"Mary":1234, "Mark":9999, "Kathy":7777}
ctuple = ()

callist = lambda alist: alist + blist
print callist([23,11,21,44])

caldict = lambda bdict: bdict.viewvalues()
print caldict({"Derek":1234, "Jeff":9012, "Kevin":5678})

print reduce(lambda calsum, elem: calsum + elem, [1, 2, 3, 4, 5], 0)   

# reduce(add, [1,2,3,4,5],0)

def ascending(a, b): return a - b
def descending(a, b): return -ascending(a, b)
print ascending(15, 12)
print descending(15, 12)

# selection sort
def s_sorted(xs, compare = ascending):
    print xs
    return [] if not xs else __select(xs, compare)


def __select(xs, compare):
    selected = xs[0]
    for elem in xs[1:]:
        if compare(elem, selected) < 0:
            print 'elem:' + str(elem)
            print 'selected:' + str(selected)
            selected = elem
        
    remain = []
    selected_list = []
    for elem in xs:
        if elem != selected:
            remain.append(elem)
        else:
            selected_list.append(elem)
            
    return xs if not remain else selected_list + __select(remain, compare)

print s_sorted([2, 1, 3, 6, 5])
print s_sorted([2, 1, 3, 6, 5], descending)

