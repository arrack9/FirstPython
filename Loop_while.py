#C:Python31python.exe  
# -*- coding:utf-8 -*-
print 'Enter two numbers...'
m = int(raw_input('Number 1: '))
n = int(raw_input('Number 2: '))
while n != 0:
    r = m % n
    m = n
    n = r
print 'GCD: {0}'.format(m)