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
